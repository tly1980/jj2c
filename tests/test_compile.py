# Sample Test passing with nose and pytest
import os
import shutil
import tempfile
import zipfile

from snapshottest import snapshot

import jj2c


FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'fixtures')


def test_compile():
  text = jj2c.compile('hello {{ name }}!', {'name': 'world'})
  assert text == 'hello world!'


def test_compile_file(snapshot):
  fpath = os.path.join(FIXTURES_DIR, 'hello.tpl')
  text = jj2c.compile_file(fpath, {'name': 'compile_file'})
  snapshot.assert_match(text)


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


def collect_contents_zip(zippath):
  dir_out = tempfile.mkdtemp()
  try:
    shutil.unpack_archive(zippath, dir_out)
    return collect_contents(dir_out)
  finally:
    shutil.rmtree(dir_out)


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


def test_compile_zip_2_zip(snapshot):
  dir_tpl = os.path.join(FIXTURES_DIR, 'a')
  dir_out = tempfile.mkdtemp()
  tpl_zip = os.path.join(dir_out, 'a.zip')
  o_zip = os.path.join(dir_out, 'o.zip')

  shutil.make_archive(tpl_zip[:-4], 'zip', dir_tpl)
  variables = {'a': 'AAA zip', 'b': 'BBB zip'}

  try:
    jj2c.compile_zip_2_zip(tpl_zip, o_zip, variables)
    snapshot.assert_match(collect_contents_zip(o_zip))
  finally:
    shutil.rmtree(dir_out)


def test_compile_dir_2_zip(snapshot):
  dir_tpl = os.path.join(FIXTURES_DIR, 'a')
  dir_out = tempfile.mkdtemp()
  o_zip = os.path.join(dir_out, 'o.zip')

  variables = {
      'a': 'AAA compile_dir_to_zip',
      'b': 'BBB compile_dir_to_zip'}

  try:
    jj2c.compile_dir_2_zip(dir_tpl, o_zip, variables)
    snapshot.assert_match(collect_contents_zip(o_zip))
  finally:
    shutil.rmtree(dir_out)


def test_compile_zip_2_dir(snapshot):
  dir_tpl = os.path.join(FIXTURES_DIR, 'a')
  dir_out = tempfile.mkdtemp()
  tpl_zip = os.path.join(dir_out, 'a.zip')

  shutil.make_archive(tpl_zip[:-4], 'zip', dir_tpl)
  variables = {'a': 'AAA zip', 'b': 'BBB zip'}

  dir_out2 = os.path.join(dir_out, 'output')

  try:
    jj2c.compile_zip_2_dir(tpl_zip, dir_out2, variables)
    snapshot.assert_match(collect_contents(dir_out2))
  finally:
    shutil.rmtree(dir_out)
