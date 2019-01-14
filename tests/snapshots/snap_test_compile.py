# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_compile_zip 1'] = {
    'b/f2': '''f2 -- BBB zip
There out her child sir his lived.''',
    'f1': '''f1 -- AAA zip
In post mean shot ye.'''
}

snapshots['test_compile_dir_to_zip 1'] = {
    'b/f2': '''f2 -- BBB compile_dir_to_zip
There out her child sir his lived.''',
    'f1': '''f1 -- AAA compile_dir_to_zip
In post mean shot ye.'''
}

snapshots['test_BatchCompiler_1 1'] = {
    'b/c/base': '''head:

base - head


body:

base - body
''',
    'b/f2': '''f2 -- BBB
There out her child sir his lived.''',
    'f1': '''head:

base - head


body:

f1 -- AAA
In post mean shot ye.
'''
}

snapshots['test_compile_dir_2_zip 1'] = {
    'b/c/base': '''head:

base - head


body:

base - body
''',
    'b/f2': '''f2 -- BBB compile_dir_to_zip
There out her child sir his lived.''',
    'f1': '''head:

base - head


body:

f1 -- AAA compile_dir_to_zip
In post mean shot ye.
'''
}

snapshots['test_compile_zip_2_zip 1'] = {
    'b/c/base': '''head:

base - head


body:

base - body
''',
    'b/f2': '''f2 -- BBB zip
There out her child sir his lived.''',
    'f1': '''head:

base - head


body:

f1 -- AAA zip
In post mean shot ye.
'''
}

snapshots['test_compile_file 1'] = '''hello compile_file!

a is 
b is '''
