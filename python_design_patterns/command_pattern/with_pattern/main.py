from create_order import CreateOrder
from update_quantity import UpdateQuantity
from ship_order import ShipOrder
from no_command import NoCommand
import sys


def get_commands():
    commands = (CreateOrder, UpdateQuantity, ShipOrder)
    return dict([cls.name, cls] for cls in commands)


def print_usage(commands):
    print("Commands : ")
    for command in commands.values():
        print("\t", command.description)


def parse_command(commands, args):
    commandName = args[0]
    command = commands.get(commandName, NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 2:
    print_usage(commands)

command = parse_command(commands, sys.argv[1:])
command.execute()
