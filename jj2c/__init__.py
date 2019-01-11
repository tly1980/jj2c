import os
import json
import logging

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


def compile_file(template_fpath, variables):
  with open(template_fpath, 'r') as f:
    return jinja2.Template(f.read()).render(**variables)


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
        with open(fname_out, 'w') as fout:
          fout.write(compile_file(fname_in, self.variables))
