#!/usr/bin/python

# Copyright: (c) 2019, knagamin
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: hello

short_description: This is my test module

version_added: "2.8"

description:
    - "This is my longer description explaining my sample module"

requirements:
    - python >= 2.7

options:
    name:
        description:
            - a name of who greeting to
        type: str
        required: true

author:
    - Kiyo Nagamine (@knagamin)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  hello:
    name: redhat
'''

RETURN = '''
message:
    description: The output message that this module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule


def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
        )
    )

    result = dict(
        changed=False,
        message=""
    )

    result['message'] = "Hello, " + module.params['name']

    module.exit_json(**result)


if __name__ == '__main__':
    main()
