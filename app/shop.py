class Shop:

    @staticmethod
    def listing_food(product_cart: dict,
                     shops: list,
                     picked_shop: str) -> None:
        total_cost = 0
        shop_cart = None
        for shop in shops:
            if shop["name"] == picked_shop:
                shop_cart = shop["products"]
        print("You have bought:")
        for key, value in product_cart.items():
            sum_for_product = value * shop_cart[key]
            if int(sum_for_product) == float(sum_for_product):
                sum_for_product = int(sum_for_product)
            print(f"{value} {key}s for {sum_for_product} dollars")
            total_cost += sum_for_product

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
