from __future__ import print_function

import collections
import json
import logging
import os
import shutil
import sys
import tempfile


__VERSION__ = '0.1.2'


try:
  from collections import OrderedDict as ODict
except Exception as e:
  ODict = dict


import jinja2
import semver
import toml
import yaml


def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)


def find_yaml_load():
  if semver.compare(yaml.__version__, '5.1.0') >= 0:
    return yaml.safe_load
  else:
    return yaml.load


class VariableExtractor(object):

  _XMAPPING = ODict([
      ('json', json.loads),
      ('yaml', find_yaml_load()),
      ('toml', toml.loads)
  ])

  def __init__(self, fname_or_content):
    self.fname_or_content = fname_or_content

  def content_str(self):
    if os.path.exists(self.fname_or_content):
      with open(self.fname_or_content, 'r') as f:
        fmt = self.fname_or_content.split('.')[-1]
        return fmt, f.read()
    else:
      return None, self.fname_or_content

  def do_parse(self, fun, text):
    _data = fun(text)
    assert isinstance(_data, dict)
    return _data

  def extract(self, format_hint=None):
    funs = ODict(self._XMAPPING)

    fmt, text = self.content_str()

    if fmt and not format_hint:
      format_hint = fmt

    if format_hint:
      assert format_hint in funs.keys()

    if format_hint:
      try:
        f = funs.pop(format_hint)
        return format_hint, self.do_parse(f, text)
      except Exception as e:
        pass

    for fname, f in funs.items():
      try:
        return fname, self.do_parse(f, text)
      except Exception as e:
        pass

    raise Exception('Unspported format')


def compile(template_str, variables, extensions):
  jj2env = jinja2.Environment(extensions=extensions)
  return jj2env.from_string(template_str).render(**variables)


class BatchCompiler(object):
  def __init__(self, variables, template_dir, output_dir, extensions):
    self.variables = variables
    self.template_dir = template_dir
    self.output_dir = output_dir
    self.jj2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(self.template_dir),
        extensions=extensions)

  def compile(self):
    os.makedirs(self.output_dir, exist_ok=True)

    for root, dirs, files in os.walk(self.template_dir):
      files = [x for x in files if not x.startswith('.')]
      for fname in files:
        dir_name = root[len(self.template_dir) + 1:]
        dir_out = os.path.join(self.output_dir, dir_name)
        if not os.path.exists(dir_out):
          os.makedirs(dir_out)
        #fname_in = os.path.join(root, fname)
        fname_tpl = os.path.join(dir_name, fname)
        fname_out = os.path.join(dir_out, fname)
        tpl = self.jj2_env.get_template(fname_tpl)
        eprint('rendering:', fname_tpl)
        if fname_out.endswith('.tpl'):
          fname_out = fname_out[:-4]
        with open(fname_out, 'w') as fout:
          tpl.stream(self.variables).dump(fout)


def compile_file(template_fpath, variables, extensions):
  with open(template_fpath, 'r') as f:
    return compile(f.read(), variables, extensions)


def compile_dir(template_dir, output_dir, variables, extensions):
  batcher = BatchCompiler(variables, template_dir, output_dir, extensions)
  batcher.compile()


def zip_folder(folder, dest_path):
  if dest_path.endswith('.zip'):
    dest_path = dest_path[:-4]
  shutil.make_archive(dest_path, 'zip', folder)


def compile_dir_2_zip(template_dir, dest_path, variables, extensions):
  dir_compile = tempfile.mkdtemp()

  try:
    compile_dir(template_dir, dir_compile, variables, extensions)
    zip_folder(dir_compile, dest_path)
  finally:
    shutil.rmtree(dir_compile)


def compile_zip_2_zip(src_path, dest_path, variables, extensions):
  dir_xtract = tempfile.mkdtemp()
  dir_compile = tempfile.mkdtemp()
  try:
    shutil.unpack_archive(src_path, dir_xtract)
    compile_dir(dir_xtract, dir_compile, variables, extensions)
    zip_folder(dir_compile, dest_path)
  finally:
    shutil.rmtree(dir_xtract)
    shutil.rmtree(dir_compile)


def compile_dir_2_zip(template_dir, dest_path, variables, extensions):
  dir_compile = tempfile.mkdtemp()

  try:
    compile_dir(template_dir, dir_compile, variables, extensions)
    zip_folder(dir_compile, dest_path)
  finally:
    shutil.rmtree(dir_compile)


def compile_zip_2_dir(template_zip, dest_path, variables, extensions):
  template_dir = tempfile.mkdtemp()

  try:
    shutil.unpack_archive(template_zip, template_dir)
    compile_dir(template_dir, dest_path, variables, extensions)
  finally:
    shutil.rmtree(template_dir)
