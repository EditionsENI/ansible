#!/bin/bash

. /tmp/ansible/bin/activate
pip install ansible --upgrade

python --version | grep 3
ansible --version
