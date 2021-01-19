from shipping_cost import ShippingCost
from shipper import FedEx, UPS, Postal


class Order:
    pass


order = Order()
shipper = FedEx()
cost_calc = ShippingCost(shipper)
cost = cost_calc.shipping_cost(order)
print(cost)
