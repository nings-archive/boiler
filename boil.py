#! /usr/bin/env python3

import argparse, os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
CLI_DESCRIPTION = 'Inserts custom boilerplate templates.'
ARGS = [
    (('name',), {
        'metavar': 'name',
        'type': str,
        'nargs': '*',
        'help': 'Name of the boilerplate template(s) to be added'
    }),
    (('-l', '--list'), {
        'action': 'store_true',
        'help': 'Lists the available boilerplate template(s)'
    })
]

def main():
    ''' Obtain a parser and its arguments, then go down the decision tree '''

    parser, args = get_cli_args()

    if args['name'] != []:
        # in the case of $ boil name [name ...]
        for name in args['name']:
            create_target_file(name)

    elif args['list']:
        # in the case of $ boil -l
        list_templates()

    else:
        # in the case of $ boil
        parser.print_usage()

def get_cli_args():
    ''' Get the CLI arguments '''
    parser = argparse.ArgumentParser(description=CLI_DESCRIPTION)
    for arg_names, options in ARGS:
        parser.add_argument(*arg_names, **options)
    return parser, vars(parser.parse_args())

def create_target_file(template_name):
    ''' Creates a file in the cwd with the name & contents of template_name '''
    with open(template_path(template_name), 'rb') as template_file:
        template_contents = template_file.read()
    with open(template_name, 'wb') as target_file:
        target_file.write(template_contents)
    print("Created ./{}".format(template_name))

def list_templates():
    ''' Lists the files in THIS_DIR/templates '''
    print(os.listdir(os.path.join(THIS_DIR, 'templates')))

def template_path(template_name):
    ''' Get the abs path to the file specified by template_name '''
    return os.path.join(THIS_DIR, 'templates/{}'.format(template_name))

if __name__ == '__main__':
    main()
