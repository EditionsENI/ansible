#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Read a properties a give it back to Ansible as an inventory

import os,argparse,json

parser = argparse.ArgumentParser(
  description='Properties converter: convert properties into Ansible inventory.'
)
parser.add_argument('--host'  , help='Get properties of machines running on specified host.')
parser.add_argument('--list'  , help='Get data of all properties machines (default: True).',
                                action='store_true', default=True)
parser.add_argument('--pretty', help='Pretty format (default: False).',
                                action='store_true', default=False)
options = parser.parse_args()

# default structure
result = {}
result['all'] = {'vars': {}, 'hosts': [] }
result['_meta'] = {'hostvars': {}}

# default empty groups
for group in [ 'apache', 'mysql' ]:
    result[group] = {'vars': {}, 'hosts': [] }

# Retrieve env value for file properties
# If not set, use default (prop2inv.properties)
properties_file = os.environ.get('PROPERTIES_FILE', 'prop2inv.properties')

# Read file then forget it
prop_file = file(properties_file)
lines = prop_file.readlines()
prop_file.close()

# Load properties in hash map
properties = {}
for line in lines:
    (k, v) = line.split('=')
    properties[k.strip()] = v.strip()

# Load db host
if properties.get('db.host'):
    result['mysql']['hosts'] = [ x.strip() for x in properties.get('db.host').split(',')]
    # Add current hosts in group 'all'
    result['all']['hosts'] += result['mysql']['hosts']

# Load Apache host
if properties.get('apache.hosts'):
    result['apache']['hosts'] = [ x.strip() for x in properties.get('apache.hosts').split(',')]
    # Add current hosts in group 'all'
    result['all']['hosts'] += result['apache']['hosts']

# Load mysql vars (if set)
for var in [ 'db.user', 'db.password' ]:
    if properties.get(var):
        # Ansible cannot use vars with '.' in there name
        ansible_var_name = var.strip().replace('.', '_')
        # Expose this variable value into mysql group
        result['mysql']['vars'][ansible_var_name] = properties.get(var).strip()

if options.pretty:
    print(json.dumps(result, sort_keys=True, indent=4))
else:
    print(json.dumps(result))
