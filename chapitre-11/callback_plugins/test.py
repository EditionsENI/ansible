# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

DOCUMENTATION = '''
    name: test
    type: stdout
    short_description: Callback test
    version_added: 2.12
    description:
        - This is a test output callback for ansible-playbook.
    extends_documentation_fragment:
      - default_callback
    requirements:
      - set as stdout in configuration
'''

class CallbackModule(CallbackModule_default):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'test'

    def __init__(self):
        # make sure the expected objects are present, calling the base's __init__
        super(CallbackModule, self).__init__()

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=False):
        return CallbackModule_default._dump_results(self, result, indent=4, sort_keys=True, keep_invocation=False)