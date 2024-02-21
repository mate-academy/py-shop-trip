from math import dist


class Shop:
    def __init__(
            self, data: dict,
            customer: dict,
            fuel_price: int | float
    ) -> None:
        self.data = data
        self.customer = customer
        self.fuel = fuel_price

    @staticmethod
    def cost_of_trip(
        distance: int | float, fuel_cons: int | float, fuel_cost: int | float
    ) -> int | float:
        return (fuel_cons * (distance * 0.01)) * fuel_cost

    @staticmethod
    def check_money(customer_cart: dict,
                    shop_price: dict
                    ) -> int | float:
        return sum(
            customer_cart[element] * shop_price[element]
            for element in customer_cart
        )

    def iter_shops(self, customer_name: str) -> tuple:
        totals_of_shop = []
        minimal_price, best_shop = None, None
        for index, shop in enumerate(self.data["shops"]):
            shop_name = shop["name"]
            fuel_cons = self.customer["car"]["fuel_consumption"]
            distance = dist(tuple(self.customer["location"]),
                            tuple(shop["location"]))
            cost_trip = Shop.cost_of_trip(distance, fuel_cons, self.fuel)
            total_eval = cost_trip * 2 + Shop.check_money(
                self.customer["product_cart"], shop["products"]
            )
            totals_of_shop.append(total_eval)

            # Check best prise considering car trip:
            if index == 0:
                minimal_price = total_eval
                best_shop = index
            elif total_eval < minimal_price:
                minimal_price = total_eval
                best_shop = index
            print(
                f"{customer_name}'s trip to the {shop_name} "
                f"costs{total_eval: .2f}"
            )
        return totals_of_shop, (minimal_price, best_shop)

    def iter_products(
        self,
        shop_data: tuple[list],
        list_prod: list,
    ) -> None:
        name = self.customer["name"]
        money = self.customer["money"]
        shop_index = shop_data[1][1]
        total_cost = 0
        best_price = shop_data[0][shop_index]
        for index, product in enumerate(list(
                self.customer["product_cart"].items())
        ):
            s_product = self.data["shops"][shop_index]["products"][product[0]]
            product_cost = product[1] * s_product
            total_cost += product_cost
            if (
                isinstance(product_cost, float)
                and str(product_cost).split(".")[1] == "0"
            ):
                product_cost = int(product_cost)
            print(f"{product[1]} {list_prod[index]} for "
                  f"{product_cost} dollars")
        print(
            f"Total cost is {total_cost} dollars\nSee you again!\n"
            f"\n{name} rides home\n"
            f"{name} now has{(money - best_price): .2f} dollars\n"
        )
