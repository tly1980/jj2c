import argparse
import json
import os
import path

import yaml

from jj2c import compile

AP = argparse.ArgumentParser()
AP.add_argument('variables', help='file pointing to variables')
AP.add_argument('template', help='file pointing to template')
AP.add_argument('-o', '--output', help='where to save the file')
AP.add_argument('-x', '--extra-variables', help='file pointing to variables')


def load_variables(fpath):
  with open(fpath, 'rb') as f:
    if fpath.endswith('.json'):
      return json.load(f)

    if fpath.endswith('.yaml'):
      return yaml.load(f)


def render_file(variables, template_f, output_f):
  template_f.read()
  pass


def main(args):

  pass


if __name__ == '__main__':
  main(AP.parse_args())
