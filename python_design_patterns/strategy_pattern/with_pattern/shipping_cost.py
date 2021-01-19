class ShippingCost():
    def __init__(self, shipper):
        self._shipper = shipper

    def shipping_cost(self, order):
        return self._shipper.calculate(order)
