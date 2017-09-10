#!/usr/bin/python
# -*- encoding: utf8 -*-
# filter to check salted passwd

import random, string

def password_generator(seed, length = 12):
    random.seed(seed)
    string_class =  string.ascii_lowercase
    string_class += string.ascii_uppercase
    string_class += string.digits
    string_class += "+-:"
    caracters = []
    for i in range(length):
        caracters += [ random.choice(string_class) ]
    return ''.join(caracters)

class FilterModule(object):
    ''' Give back filters to Ansible '''

    def filters(self):
        return {
            'password_generator': password_generator
        }
