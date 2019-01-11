import json
import logging
import os
import shutil
import tempfile

import jinja2

import yaml
import toml


class VariableExtractor(object):
  def __init__(self, fname_or_content):
    self.fname_or_content = fname_or_content
    self.data = None

  def content_str(self, fname_or_content):
    if os.path.exists(fname_or_content):
      with open(fname_or_content, 'rb') as f:
        return f.read()

  def extract(self):
    funs = [yaml.load, toml.loads, json.loads]
    content_str = self.content_str()
    for f in funs:
      try:
        self.data = f(content_str)
        return self.data
      except Exception as e:
        raise e


def compile(template_str, variables):
  return jinja2.Template(template_str).render(**variables)


class BatchCompiler(object):
  def __init__(self, variables, template_dir, output_dir):
    self.variables = variables
    self.template_dir = template_dir
    self.output_dir = output_dir

  def compile(self):
    for root, dirs, files in os.walk(self.template_dir):
      for fname in files:
        dir_name = root[len(self.template_dir) + 1:]
        dir_out = os.path.join(self.output_dir, dir_name)
        if not os.path.exists(dir_out):
          os.makedirs(dir_out)
        fname_in = os.path.join(root, fname)
        fname_out = os.path.join(dir_out, fname)
        if fname_out.endswith('.tpl'):
          fname_out = fname_out[:-4]
        with open(fname_out, 'w') as fout:
          fout.write(compile_file(fname_in, self.variables))


def compile_file(template_fpath, variables):
  with open(template_fpath, 'r') as f:
    return jinja2.Template(f.read()).render(**variables)


def compile_dir(template_dir, output_dir, variables):
  batcher = BatchCompiler(variables, template_dir, output_dir)
  batcher.compile()


def zip_folder(folder, dest_path):
  if dest_path.endswith('.zip'):
    dest_path = dest_path[:-4]
  shutil.make_archive(dest_path, 'zip', folder)


def compile_dir_2_zip(template_dir, dest_path, variables):
  dir_compile = tempfile.mkdtemp()

  try:
    compile_dir(template_dir, dir_compile, variables)
    zip_folder(dir_compile, dest_path)
  finally:
    shutil.rmtree(dir_compile)


def compile_zip_2_zip(src_path, dest_path, variables):
  dir_xtract = tempfile.mkdtemp()
  dir_compile = tempfile.mkdtemp()
  try:
    shutil.unpack_archive(src_path, dir_xtract)
    compile_dir(dir_xtract, dir_compile, variables)
    zip_folder(dir_compile, dest_path)
  finally:
    shutil.rmtree(dir_xtract)
    shutil.rmtree(dir_compile)
