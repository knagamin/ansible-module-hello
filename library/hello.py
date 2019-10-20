#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
module: hello
short_descriptioin: "Make a greeting"
'''


def run_module():
    module_args = dict(
        name=dict(required=True, type='str'),
        period=dict(reuiqred=False,
                    type='str',
                    choices=['morning', 'noon', 'evening'],
                    default='noon',
                    )
    )

    period_phrases = {'morning': 'Good morning', 'noon': 'Hello', 'evening': 'Good evening'}

    module = AnsibleModule(
                argument_spec=module_args,
                supports_check_mode=True
    )

    response = {"greet": period_phrases[module.params['period']] + ", " + module.params['name'] + "!"}
    module.exit_json(changed=False, meta=response)


def main():
    run_module()


if __name__ == '__main__':
    main()
