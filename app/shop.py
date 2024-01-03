class Shop:
    def __init__(self, product_cart: dict, shops: list):
        self.product_cart = product_cart
        self.shops = shops

    def listing_food(self, picked_shop: str) -> None:
        total_cost = 0
        shop_cart = None
        for shop in self.shops:
            if shop["name"] == picked_shop:
                shop_cart = shop["products"]
        print("You have bought:")
        for food, counts in self.product_cart.items():
            sum_for_product = counts * shop_cart[food]
            if int(sum_for_product) == float(sum_for_product):
                sum_for_product = int(sum_for_product)
            print(f"{counts} {food}s for {sum_for_product} dollars")
            total_cost += sum_for_product

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
