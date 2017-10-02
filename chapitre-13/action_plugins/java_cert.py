#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from ansible.plugins.action import ActionBase
from ansible.constants import mk_boolean as boolean

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        ''' handler for java_cert operations '''
        if task_vars is None:
            task_vars = dict()

        if not tmp:
            tmp = self._make_tmp_path()

        result = super(ActionModule, self).run(tmp, task_vars)

        cert_path = self._task.args.get('cert_path', None)
        remote_src = boolean(self._task.args.get('remote_src', True))

        # remove remote_src from module argument
        new_module_args = self._task.args.copy()
        if 'remote_src' in new_module_args:
            del new_module_args['remote_src']

        if not remote_src:
            # transfer the file to a remote tmp location
            tmp_src = self._connection._shell.join_path(tmp, cert_path)
            self._transfer_file(cert_path, tmp_src)
            # fix file permissions when copy is done as a different user
            self._fixup_perms2((tmp, tmp_src))
            # Update cert_path value.
            new_module_args.update(dict(cert_path=tmp_src))

        # execute the java_cert module now, with the updated args
        result.update(self._execute_module(module_args=new_module_args, task_vars=task_vars))
        # clean up tmp
        self._remove_tmp_path(tmp)
        return result
