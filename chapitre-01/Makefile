VERSION         ?= 2.9.2
ANSIBLE_VERSION ?= ansible-$(VERSION)
ANSIBLE_DIR     ?= $$HOME/$(ANSIBLE_VERSION)

install:
	wget https://releases.ansible.com/ansible/ansible-$(VERSION).tar.gz -O - | (cd $$HOME && tar xfz -)

install-release:
	./launch-ansible.sh | grep $(VERSION)

virtual-env:
	virtualenv --python=python3 /tmp/ansible
	./install-virtualenv.sh

all: install install-release
