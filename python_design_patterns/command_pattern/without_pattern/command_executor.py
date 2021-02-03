class CommandExecutor:
    def __init__(self):
        pass

    def execute_command(self, args):
        command = args[0]
        if command == "CreateOrder":
            self.create_order()
        elif command == "UpdateQuantity":
            newQuantity = args[1]
            self.update_quantity(newQuantity)
        elif command == "ShipOrder":
            self.ship_order()
        else:
            print(F"Unrecognised command : {command}")

    def create_order(self):
        print("order created")

    def ship_order(self):
        print("order shipped")

    def update_quantity(self, newQuantity):
        print(F"quantity updated --> {newQuantity}")
