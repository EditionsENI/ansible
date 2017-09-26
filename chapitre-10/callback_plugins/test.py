# -*- coding: utf-8 -*-

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

import json

class CallbackModule(CallbackModule_default):
    CALLBACK_VERSION = 2.0
    CALLBACK_NAME = 'test'

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=False):
        return CallbackModule_default._dump_results(self, result, indent=4, sort_keys=True, keep_invocation=False)
