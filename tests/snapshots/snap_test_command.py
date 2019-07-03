# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_lines_as_array_inspect 1'] = '''## My List 1
1 - a
2 - bb
3 - ccc
4 - dddd


## My List 2
1 - eeee
2 - fff
3 - gg
4 - h
'''

snapshots['test_lines_as_array 1'] = '''## My List 1
1 - a
2 - bb
3 - ccc
4 - dddd


## My List 2
1 - eeee
2 - fff
3 - gg
4 - h
'''
