import sys
from command_executor import CommandExecutor

if len(sys.argv) < 2:
    print("Usage : python -m main.py <command>")
    print("Commands : ")
    print("\tCreateOrder")
    print("\tUpdateQuantity <number>")
    print("\tShipOrder")
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])
