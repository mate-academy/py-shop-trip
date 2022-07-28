import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def go_shopping(self, fuel_price: float, shops: dict):
        print(f"{self.name} has {self.money} dollars")
        options = {}
        for shop in shops.values():
            options[shop.name] = shop.get_shopping_cost(self.location,
                                                        self.product_cart,
                                                        self.car,
                                                        fuel_price)
        for key, value in options.items():
            print(f"{self.name}'s trip to the {key} costs {value}")

        if self.money < min(options.values()):
            print((f"{self.name} doesn't "
                   f"have enough money to make purchase in any shop"))
        else:
            key_list = list(options.keys())
            values_list = list(options.values())
            cheapest_shop = key_list[values_list.index(min(options.values()))]
            print(f"{self.name} rides to {cheapest_shop}\n")
            shops[cheapest_shop].visit_cheapest_shop(self.name,
                                                     self.product_cart)
            print(f"{self.name} rides home")
            self.money -= min(options.values())
            print(f"{self.name} now has {self.money} dollars\n")
