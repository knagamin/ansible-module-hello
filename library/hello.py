#!/usr/bin/python

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
