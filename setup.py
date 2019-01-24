from codecs import open
from os import path
from setuptools import setup, find_packages
import re


module_name = 'jj2c'
with open("{name}/__init__.py".format(name=module_name), encoding='utf-8') as f:
  __version__ = re.search(
    '^__version__\s*=\s*[\'\"]([^\'\"]+)', f.read(),
    flags=re.I | re.M).group(1)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
  all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='jj2c',
    version=__version__,
    description='Jinja2 compiler',
    long_description=long_description,
    url='https://github.com/tly1980/jj2c',
    download_url='https://github.com/tly1980/jj2c/tarball/' + __version__,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tom Tang',
    scripts=['bin/jj2c'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='tly1980@gmail.com'
)
