# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_lines_as_array 1'] = b'>> my_lst\n1 - a\n2 - bb\n3 - ccc\n4 - dddd\n\n\n>> my_lst2\n1 - eeee\n2 - fff\n3 - gg\n4 - h\n'
