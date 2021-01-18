from no_strategy import Order, Shipper, ShippingCost

order = Order(Shipper.fedex)
costCalculator = ShippingCost()

cost = costCalculator.shipping_cost(order)

print(F"Fedex shpping cost --> {cost}")     