from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int

    def trip_costs(self, shop: object, car: object) -> tuple:
        point_x = shop.location[0] - self.location[0]
        point_y = shop.location[1] - self.location[1]
        distance = (point_x ** 2 + point_y ** 2) ** 0.5
        distance_cost = car.distance_cost(distance)

        products_cost = 0
        for product, amount in self.product_cart.items():
            products_cost += shop.products[product] * amount

        return products_cost, distance_cost + products_cost

    def analysis_of_shops(self, shops: list, car: object) -> list:
        can_go = True
        shops_data = {}

        for shop in shops:
            total_costs = self.trip_costs(shop, car)[1]
            if self.money < total_costs:
                can_go = False
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {total_costs}")
            shops_data[shop.name] = total_costs
        choice = min(shops_data, key=shops_data.get)
        if can_go:
            print(f"{self.name} rides to {choice}\n")
            return [shop for shop in shops if shop.name == choice]
        print(f"{self.name} doesn't have "
              f"enough money to make purchase in any shop")
