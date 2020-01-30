#!/usr/bin/env python
# -*- coding: utf-8 -*-
# db_schema - based on dataset and sqlalchemy

from ansible.module_utils.basic import AnsibleModule, iteritems

import yaml, dataset
from sqlalchemy import String

def main():
    module = AnsibleModule(
        argument_spec=dict(
            db_url = dict(required=True, type='str'),
            spec   = dict(required=True, type='json'),
            state  = dict(default="present", choices=[ "present" ]),
        ),
        supports_check_mode=True
    )
    db_url = module.params.get('db_url')
    spec   = module.params.get('spec')
    state  = module.params.get('state')

    changed = False
    db = dataset.connect(db_url)
    # What we got before starting modifications?
    before = dict(tables=db.tables, columns=[])
    after  = dict(tables=db.tables, columns=[])

    yaml_spec = yaml.load(spec)

    # Read yaml spec and apply it to current database
    for table, columns in iteritems(yaml_spec):
        if table not in db.tables:
            if not module.check_mode:
                new_table = db[table]
            changed = True
            if not module.check_mode:
                after['tables'].append(table)
        else:
            # We store columns before modification
            table_columns = []
            for c in db[table].columns:
                table_columns.append("%s.%s" % (table, c))
            before['columns'] += table_columns
            after ['columns'] += table_columns
        for column in columns:
            if column not in db[table].columns:
                # New columns
                after['columns'].append("%s.%s" % (table, column))
                if not module.check_mode:
                    db[table].create_column(column, String())
                changed=True

    module.exit_json(
      changed=changed,
      diff=dict(
        before=before,
        after=after
      )
    )

if __name__ == '__main__':
    main()
