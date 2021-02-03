from abstract_command import AbstractCommand


class NoCommand(AbstractCommand):

    name = "ShipOrder"
    description = "ShipOrder"

    def __init__(self, args):
        self._command = args[0]

    def execute(self):
        print(F"Unknown command {self._command}")
