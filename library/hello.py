#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule


def run_module():

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


def main():
    run_module()


if __name__ == '__main__':
    main()
