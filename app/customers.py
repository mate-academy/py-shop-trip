from app.data import cust_list, fuel_price


class Customer:
    def __init__(
            self,
            name,
            prod_cart,
            loc,
            money,
            fuel_cons
    ):
        self.name = name
        self.prod_cart = prod_cart
        self.loc = loc
        self.money = money,
        self.fuel_cons = fuel_cons

    def dist(self, shop):
        return (
            (self.loc[0] - shop.loc[0]) ** 2 + (self.loc[1] - shop.loc[1]) ** 2
        ) ** 0.5

    def riding(self, shop):
        return round(
            self.fuel_cons / 100 * self.dist(shop) * fuel_price * 2, 2
        )

    def shopping(self, shop):
        prods = list(self.prod_cart.keys())
        prods_count = list(self.prod_cart.values())
        pc = prods_count  # --> flake8 max-line-length = 79
        prods_costs = [prod * shop.prices[i] for i, prod in enumerate(pc)]
        shopping_cost = sum(prods_costs)
        total_cost = shopping_cost + self.riding(shop)

        return [
            self.name,
            self.money[0],
            shop.name,
            prods_count,
            prods,
            prods_costs,
            shopping_cost,
            total_cost
        ]


custs = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"]["fuel_consumption"]
    )
    for customer in cust_list
]
