VERSION         ?= 2.9.2
ANSIBLE_VERSION ?= ansible-$(VERSION)
ANSIBLE_DIR     ?= $$HOME/$(ANSIBLE_VERSION)

install:
	wget https://releases.ansible.com/ansible/ansible-$(VERSION).tar.gz -O - | (cd $$HOME && tar xfz -)

tests:
	./launch-ansible.sh

all: install tests
