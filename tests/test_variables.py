import os


import jj2c


FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'fixtures')


def test_basic_yaml_as_str():
  ve = jj2c.VariableExtractor('a: 123')
  assert ve.extract() == ('yaml', {'a': 123})


def test_basic_json_as_str():
  ve = jj2c.VariableExtractor('{"a": 123}')
  assert ve.extract() == ('json', {'a': 123})


def test_basic_toml_as_str():
  ve = jj2c.VariableExtractor('a=123')
  assert ve.extract() == ('toml', {'a': 123})


def test_basic_toml_as_str():
  ve = jj2c.VariableExtractor('a=123')
  assert ve.extract() == ('toml', {'a': 123})


def test_basic_yaml_as_file(snapshot):
  vars_file = os.path.join(FIXTURES_DIR, 'vars.yaml')
  ve = jj2c.VariableExtractor(vars_file)
  fmt, data = ve.extract()
  assert fmt == 'yaml'
  snapshot.assert_match(data)


def test_basic_json_as_file(snapshot):
  vars_file = os.path.join(FIXTURES_DIR, 'vars.json')
  ve = jj2c.VariableExtractor(vars_file)
  fmt, data = ve.extract()
  assert fmt == 'json'
  snapshot.assert_match(data)


def test_basic_toml_as_file(snapshot):
  vars_file = os.path.join(FIXTURES_DIR, 'vars.toml')
  ve = jj2c.VariableExtractor(vars_file)

  fmt, data = ve.extract()
  assert fmt == 'toml'
  snapshot.assert_match(data)
