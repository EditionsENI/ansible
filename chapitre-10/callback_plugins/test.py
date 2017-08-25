# -*- coding: utf-8 -*-

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default
from ansible import constants as C

class CallbackModule(CallbackModule_default):
    pass
