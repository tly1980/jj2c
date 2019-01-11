# Sample Test passing with nose and pytest
import os
import tempfile
import shutil

#from snapshottest import snapshot

import jj2c


FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'fixtures')


def test_compile():
  text = jj2c.compile('hello {{ name }}!', {'name': 'world'})
  assert text == 'hello world!'


def test_compile_file():
  fpath = os.path.join(FIXTURES_DIR, 'hello.tpl')
  text = jj2c.compile_file(fpath, {'name': 'compile_file'})
  assert text == 'hello compile_file!'


def collect_contents(folder):
  contents = {}
  for root, dirs, files in os.walk(folder):
    for fname in files:
      dir_name = root[len(folder) + 1:]
      fname_key = os.path.join(dir_name, fname)
      fname_real = os.path.join(root, fname)
      with open(fname_real, 'r') as f:
        contents[fname_key] = f.read()
  return contents


def test_BatchCompiler_1(snapshot):
  dir_tpl = os.path.join(FIXTURES_DIR, 'a')
  dir_out = tempfile.mkdtemp()
  variables = {'a': 'AAA', 'b': 'BBB'}
  try:
    batch = jj2c.BatchCompiler(variables, dir_tpl, dir_out)
    batch.compile()
    snapshot.assert_match(
        collect_contents(dir_out))
  finally:
    shutil.rmtree(dir_out)
