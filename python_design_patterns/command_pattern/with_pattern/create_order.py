from abstract_command import AbstractCommand
from abstract_order_command import AbstractOrderCommand


class CreateOrder(AbstractCommand, AbstractOrderCommand):

    name = "CreateOrder"
    description = "CreateOrder"

    def __init__(self, args):
        pass

    def execute(self):
        print(F"created order")
