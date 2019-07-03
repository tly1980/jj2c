import subprocess
import sys
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FIXTURES_DIR = os.path.join(DIR_PATH, 'fixtures')


def test_version():
  subprocess.check_output(['bin/jj2c', '--help'])


def test_lines_as_array(snapshot):
  tpl = os.path.join(FIXTURES_DIR, 'lines_array.tpl')
  lst1_txt = os.path.join(FIXTURES_DIR, 'lst1.txt')
  lst2_txt = os.path.join(FIXTURES_DIR, 'lst2.txt')
  cmd = [
      'bin/jj2c',
      tpl,
      '--lines_as_array',
      'lst1=%s' % lst1_txt,
      'lst2=%s' % lst2_txt
  ]
  output = subprocess.check_output(cmd)
  snapshot.assert_match(output)
