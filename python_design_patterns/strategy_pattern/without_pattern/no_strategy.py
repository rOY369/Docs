from enum import Enum


class Order():
    def __init__(self, shipper):
        self._shipper = shipper

    @property
    def shipper(self):
        return self._shipper


class Shipper(Enum):
    fedex = 1
    ups = 2
    postal = 3


class ShippingCost():
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost
        elif order.shipper == Shipper.ups:
            return self._ups_cost
        elif order.shipper == Shipper.postal:
            return self._postal_cost
        else:
            raise ValueError("invalid shipper")

    @property
    def _fedex_cost(self):
        return 3.0

    @property
    def _ups_cost(self):
        return 4.0

    @property
    def _postal_cost(self):
        return 5.0
