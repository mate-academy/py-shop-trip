from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: dict

    def cost_trip_shop(self, shop_loc: list[int], fuel_price: float) -> float:
        dist = (((shop_loc[0] - self.location[0]) ** 2
                 + (shop_loc[1] - self.location[1]) ** 2) ** 0.5)
        return round(self.car["fuel_consumption"] / 100 * dist * fuel_price, 2)

    def cost_product_shop(self, shop_products: dict) -> float:
        total_cost = 0
        for product, count in self.product_cart.items():
            total_cost += shop_products[product] * count

        return total_cost
