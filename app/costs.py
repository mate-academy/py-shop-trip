class Costs:
    @staticmethod
    def cost_of_trip(distance: int | float,
                     fuel_cons: int | float,
                     fuel_cost: int | float) -> int | float:
        return (fuel_cons * (distance * 0.01)) * fuel_cost

    @staticmethod
    def check_money(customer_cart: dict,
                    shop_price: dict) -> int | float:
        customer = list(customer_cart.values())
        shop = list(shop_price.values())
        _sum = 0
        for element in range(len(customer)):
            _sum += customer[element] * shop[element]
        return _sum
