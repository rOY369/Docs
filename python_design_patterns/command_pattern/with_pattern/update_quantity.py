from abstract_command import AbstractCommand
from abstract_order_command import AbstractOrderCommand


class UpdateQuantity(AbstractCommand, AbstractOrderCommand):

    name = "UpdateQuantity"
    description = "UpdateQuantity <number>"

    def __init__(self, args):
        self.newQuantity = args[1]

    def execute(self):
        print(F"quantity updated --> {self.newQuantity}")
