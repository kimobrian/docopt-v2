#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    operations add <numA> <numB>
    operations add_multiple [<numbers>...]
    operations operation <numA> <numB> <sign>
    operations parents (--father=<ans> | --mother=<ans>)
    operations name [--fname=<f_name>] [--lname=<l_name>]
    operations (-i | --interactive)
    operations (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --fname First name
    --lname Last name
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from functions import Operations

ops = Operations();


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'DOCOPT V2.0 EXAMPLE' \
        + ' (type help for a list of commands.)'
    prompt = '((ops>> '
    file = None

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <numA> <numB>"""
        num_a = arg['<numA>'] #Using sigle required qrguments
        num_b = arg['<numB>']
        ops.add(num_a, num_b)

    @docopt_cmd
    def do_add_multiple(self, arg):
        """Usage: add_multiple [<numbers>...]"""
        numbers = arg['<numbers>'] # Demonstrate optional and multiple arguments. Command can be called with or without arguments
        print(ops.add_multiple(numbers))

    @docopt_cmd
    def do_operation(self, arg):
        """Usage: operation <numA> <numB> <sign>"""
        num_a = arg['<numA>'] #Using sigle required qrguments
        num_b = arg['<numB>']
        sign = arg['<sign>']
        print(ops.multiple_operations(num_a, num_b, sign))

    @docopt_cmd
    def do_name(self, arg):
        """Usage: name [--fname=<f_name>] [--lname=<l_name>]"""
        first_name = arg['--fname'] #Using sigle required qrguments
        last_name = arg['--lname']
        if not first_name and last_name:
            print(ops.func_default_values(last_name = last_name))
        elif first_name and not last_name:
            print(ops.func_default_values(first_name = first_name))
        elif not first_name and not last_name:
            print(ops.func_default_values())
        else:
            print(ops.func_default_values(first_name, last_name))

    @docopt_cmd
    def do_parents(self, arg):
        """Usage: parents (--mother=<ans> | --father=<ans>)"""
        father_name = arg['--father'] #Using or functionality
        mother_name = arg['--mother']
        if not father_name:
            print("Your mother's name is {0}".format(mother_name))
        else:
            print("Your father's name is {0}".format(father_name))


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        MyInteractive().cmdloop()
    except KeyboardInterrupt:
        print("Exiting Application")
