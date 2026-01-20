from __future__ import annotations


class Shop:
    def __init__(self, *args, **kwargs) -> None:
        # name, location, products

        shop = None
        if args and isinstance(args[0], dict):
            shop = args[0]
        elif isinstance(kwargs, dict):
            shop = kwargs

        if shop is not None:
            self.name = shop["name"]
            self.location = shop["location"]

            self.products = []
        else:
            raise TypeError

    def setproduct(self, products: list) -> None:
        self.products = products

    @staticmethod
    def get_list_shops(shops_info: dict) -> list(Shop):
        shops = []
        for shop_info in shops_info:
            shop = Shop(shop_info)

            shop.setproduct(shop_info["products"])

            shops.append(shop)
        return shops

    def visit_store(self, customer: object) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        result_amount = 0
        for demand, demand_quantity in customer.product_cart.items():
            amount = demand_quantity * self.products[demand]
            if demand_quantity > 1:
                print(f"{demand_quantity} {demand}s for {amount} dollars")
            else:
                print(f"{demand_quantity} {demand} for {amount} dollars")
            result_amount += amount
        print(f"Total cost is {result_amount} dollars")
        print("See you again!\n")
        return result_amount
