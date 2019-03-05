jj2c
===============================

version number: {{ version }}
author: Tom Tang

Overview
--------

Jinja2 compiler

Installation / Usage
--------------------

To install use pip:

    $ pip install jj2c


To use it:

Render from folder to folder:
    `jj2c template_folder/ -V 'a: AAA' 'b: BBB' -o output_folder/`

Render from zip to folder:
    `jj2c template.zip -V 'a: AAA' 'b: BBB' -o output_folder/`

Render from zip to zip:
    `jj2c template.zip -V 'a: AAA' 'b: BBB' -o template.zip`

Render to stdout:
    `jj2c template-file -V 'a: AAA' 'b: BBB'`

Or clone the repo:

    $ git clone https://github.com/tly1980/jj2c.git
    $ python setup.py install


Using Jinja2 extendsions
------------------------

Let say you have a `use_do.tpl` with following contents:

```
{%- set a = [] -%}
{%- do a.append(1) -%}
{%- do a.append(2) -%}
{%- do a.append(name) -%}
{{ a }}
```

In order to render those content properly you will need
`jinja2.ext.do` extension.

Use `-e` or `--extensions` tags to specify the extensions. And you can specify
more than one.

```
jj2c tests/fixtures/use_do.tpl -V 'name: jack' -e jinja2.ext.do jinja2.ext.i18n
```

Output is:
```

Using extensions: ['jinja2.ext.do', 'jinja2.ext.i18n']
Compiling... file to stdout
src: tests/fixtures/use_do.tpl
dest:-
[1, 2, 'jack']
```


Contributing
------------

TBD

Example
-------

TBD

