from abstract_command import AbstractCommand
from abstract_order_command import AbstractOrderCommand


class ShipOrder(AbstractCommand, AbstractOrderCommand):

    name = "ShipOrder"
    description = "ShipOrder"

    def __init__(self, args):
        pass

    def execute(self):
        print(F"shipped order")
