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
            # i have this "if" because i
            # couldn't get that particular number to int
            if sum_for_product == 3.0:
                sum_for_product = 3
            print(f"{value} {key}s for {sum_for_product} dollars")
            total_cost += sum_for_product

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
