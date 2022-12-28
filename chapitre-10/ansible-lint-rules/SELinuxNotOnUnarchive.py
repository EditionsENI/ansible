from ansiblelint.rules import AnsibleLintRule


class SELinuxNotOnUnarchive(AnsibleLintRule):
    id = 'no-setype-on-unarchive'
    shortdesc = 'setype not on unarchive'
    description = 'No field ``setype`` on ``unarchive`` module'
    tags = ["unarchive"]

    def matchtask(self, task, file):
        module = task["action"]["__ansible_module__"]
        return module == "unarchive" and \
               'setype' not in task['action']
