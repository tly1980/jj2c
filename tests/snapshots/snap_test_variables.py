# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['test_basic_yaml_as_file 1'] = {
    'a': 'AAA',
    'b': 'BBB',
    'name': 'yaml vars file'
}

snapshots['test_basic_json_as_file 1'] = {
    'a': 'AAAjson',
    'b': 'BBBjson',
    'name': 'json vars file'
}

snapshots['test_basic_toml_as_file 1'] = {
    'database': {
        'connection_max': 5000,
        'ports': [
            8001,
            8001,
            8002
        ],
        'server': '192.168.1.1'
    },
    'owner': {
        'dob': GenericRepr("datetime.datetime(1979, 5, 27, 7, 32, tzinfo=<toml.tz.TomlTz object at 0x10b74f390>)"),
        'name': 'Tom Preston-Werner'
    },
    'title': 'TOML 例子'
}
