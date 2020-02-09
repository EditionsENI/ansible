import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_httpd_is_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed


def test_httpd_is_running(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
