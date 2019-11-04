#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule


def run_module():

    module = AnsibleModule(
        argument_spec=dict(
                name=dict(type='str', required=True),
        )
    )

    msg = "Hello, " + module.params['name']

    response = {"msg": msg}
    module.exit_json(changed=False, greeting=response)


def main():
    run_module()


if __name__ == '__main__':
    main()
