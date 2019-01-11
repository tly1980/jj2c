# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_BatchCompiler_1 1'] = {
    'b/f2.tpl': '''f2 -- BBB
There out her child sir his lived.''',
    'f1.tpl': '''f1 -- AAA
In post mean shot ye.'''
}
