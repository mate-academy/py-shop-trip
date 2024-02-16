from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def make_purchase(self, shop_products: dict) -> None:
        total_cost = 0.0

        print(f"Date: 04/01/2021 12:33:41\n"
              f"Thanks, {self.name}, for your purchase!\nYou have bought:")
        for product, amount in self.product_cart.items():
            if product in shop_products:
                price = shop_products[product] * amount
                price = int(price) if price == int(price) else price
                total_cost += price
                print(f"{amount} {product}s for {price} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!")
