MODULE_DIR=ansible/lib/ansible/modules/my_modules
INIT_PY=${MODULE_DIR}/__init__.py

.PHONY: sanity-test

sanity-test: ${MODULE_DIR}
	touch ${MODULE_DIR}/__init__.py
	cp library/hello.py ${MODULE_DIR}/
	pip install --user -r ansible/requirements.txt
	cd ansible && . hacking/env-setup && ansible-test sanity --python 2.7 hello


${MODULE_DIR}:
	mkdir ${MODULE_DIR}
