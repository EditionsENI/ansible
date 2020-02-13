# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

DOCUMENTATION = '''
  callback: test
  callback_type: stdout
  requirements:
  short_description: Adds time to play stats
  version_added: "2.0"
  description:
      - This callback is a test.
  options:
'''

class CallbackModule(CallbackModule_default):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'test'

    def v2_runner_on_start(self, host, task):
        pass

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=False):
        return CallbackModule_default._dump_results(self, result, indent=4, sort_keys=True, keep_invocation=False)
