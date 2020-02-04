from ansiblelint import AnsibleLintRule


class SELinuxNotOnUnarchive(AnsibleLintRule):
    id = '9001'
    shortdesc = 'setype not on unarchive'
    description = 'No field ``setype`` on ``unarchive`` module'
    tags = ["unarchive"]

    def matchtask(self, file, task):
        module = task["action"]["__ansible_module__"]
        return module == "unarchive" and \
               'setype' not in task['action']
