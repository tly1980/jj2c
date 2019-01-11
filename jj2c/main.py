#!/usr/bin/env python

from __future__ import print_function

import argparse
import json
import os
import sys

import yaml

import jj2c

AP = argparse.ArgumentParser()
AP.add_argument(
    'var_file', help='file pointing to variables, can be either json or yaml')
AP.add_argument('template', help='file pointing to template')
AP.add_argument('-o', '--output', default='-', help='where to save the file')
AP.add_argument('-x', '--extra_variables', default=None, help='file pointing to variables')


def is_tpl(fpath):
  if not os.path.isfile(fpath):
    raise Exception('No such *FILE*: %s' % fpath)
  return not fpath.endswith('.zip')


def load_variables_str(text):
  try:
    return yaml.load(text)
  except:
    return json.loads(text)


def load_variables(fpath):
  with open(fpath, 'rb') as f:
    if fpath.endswith('.json'):
      return json.load(f)

    if fpath.endswith('.yaml'):
      return yaml.load(f)


def dump_file(fpath, content):
  if fpath == '-':
    sys.stdout.write(content)
    sys.stdout.flush()
  else:
    with open(fpath) as f:
      f.write(content)


def main(args):
  variables = load_variables(args.var_file)
  if args.extra_variables:
    x_variables = load_variables_str(args.extra_variables)
    variables.update(x_variables)

  if is_tpl(args.template):
    with open(args.template) as f:
      dump_file(args.output, jj2c.compile(f.read(), variables))
  elif args.template.endswith('.zip') and args.output.endswith('.zip'):
    jj2c.compile_zip_2_zip(args.template, args.output)
  elif args.output.endswith('.zip'):
    jj2c.compile_dir_2_zip(args.template, args.output)
  elif not args.template.endswith('.zip') and not args.output.endswith('.zip'):
    jj2c.compile_dir(args.template, args.output)
  else:
    print('Unsupported')


if __name__ == '__main__':
  main(AP.parse_args())
