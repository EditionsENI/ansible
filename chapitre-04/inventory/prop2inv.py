#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Read a properties a give it back to Ansible as an inventory

from ansible.plugins.inventory import BaseInventoryPlugin

class InventoryModule(BaseInventoryPlugin):

    NAME = 'prop2inv'

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(
          inventory, loader, path, cache
        )
        config = self._read_config_data(path)
        properties_file = config.get("properties_file",
                                     "prop2inv.properties")

        # Load properties in hash map
        properties = {}
        with open(properties_file) as p:
            for line in p.readlines():
                (k, v) = line.split('=')
                properties[k.strip()] = v.strip()

        self.inventory.add_group("mysql")
        self.inventory.add_group("apache")

        # Load db host
        if properties.get('db.host'):
            for host in properties.get('db.host').split(','):
                self.inventory.add_host(host.strip(), group="mysql")

        # Load Apache host
        if properties.get('apache.hosts'):
            for host in properties.get('apache.hosts').split(','):
                self.inventory.add_host(host.strip(), group="apache")

        # Load mysql vars (if set)
        for var in [ 'db.user', 'db.password' ]:
            if properties.get(var):
                # Ansible cannot use vars with '.' in there name
                ansible_var_name = var.strip().replace('.', '_')
                # Expose this variable value into mysql group
                value = properties.get(var).strip()
                self.inventory.set_variable(
                  "mysql", ansible_var_name, value
                )
