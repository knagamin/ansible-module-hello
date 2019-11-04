#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            hour=dict(type='int'),
        )
    )

    result = dict(
        changed=False,
        message=""
    )

    result['message'] = "Hello, {}.".format(module.params['name'])

    if module.params['hour'] is not None:
        result['message'] = "{} It's {} o'clock".format(
            result['message'],
            module.params['hour']
        )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
