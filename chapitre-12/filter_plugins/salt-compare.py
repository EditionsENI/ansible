#!/usr/bin/python
# -*- encoding: utf8 -*-
# filter to check salted passwd

import crypt

def checkpw(plain_text, hashed_test):
    return crypt.crypt(plain_text, hashed_test) == hashed_test

class FilterModule(object):
    ''' Give back filters to Ansible '''

    def filters(self):
        return {
            'checkpw': checkpw
        }
