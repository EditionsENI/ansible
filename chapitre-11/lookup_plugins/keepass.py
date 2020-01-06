#!/usr/bin/python
# -*- encoding: utf8 -*-

from ansible.plugins.lookup import LookupBase

from pykeepass import PyKeePass

def get_passwords(filename, master_key, entry):
    db = PyKeePass(filename, password=master_key)
    results = []
    for entry in db.find_entries_by_username(entry):
        results.append({
          'user':     entry.username,
          'password': entry.password
        })
    return results

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        keepass_db = terms.pop(0)
        password = terms.pop(0)
        query = terms.pop(0)
        return get_passwords(keepass_db, password, query)
