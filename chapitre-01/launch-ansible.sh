#!/bin/sh

set -x
. ./ansible-v2.9.2

python3 $ANSIBLE_HOME/bin/ansible --version
