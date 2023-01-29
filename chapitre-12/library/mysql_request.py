#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION='''
module: mysql_request
author: Yannig Perré
description: Module to do simple SQL request against MySQL database

options:
  db_name:
    description: DB name
    required: yes
  request:
    description: SQL request to execute
    required: yes

'''

EXAMPLES='''
- name: "Simple SELECT"
  mysql_request:
    db_name: "test"
    request: "SELECT 1"
'''

RETURN = '''
results:
    description: return all results
'''

from ansible.module_utils.basic import AnsibleModule
import pymysql

def main():
    module = AnsibleModule(
        argument_spec=dict(
            db_name    = dict(required=True, type='str'),
            request    = dict(required=True, type='str'),
        )
    )

    # Retrieving options value
    db_name  = module.params.get('db_name')
    request  = module.params.get('request')

    # Connect to your database
    db = pymysql.connect(db=db_name)
    # Get a cursor, execute your request then close connection
    cur = db.cursor()
    cur.execute(request)
    results = cur.fetchall()
    db.close()
    # Return result
    module.exit_json(
      changed=False,
      ansible_facts=dict(
        mysql_results=results
      )
    )

if __name__ == "__main__":
    main()
