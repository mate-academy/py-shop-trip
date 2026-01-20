class Shop:
    def __init__(self, name: str, products: dict, location: list) -> None:
        self.name = name
        self.price_list = products
        self.location = location

    def calculate_purchase_cost(self, products_to_buy: dict) -> float:
        return round(sum([self.price_list[product_name]
                          * products_to_buy[product_name]
                          for product_name in products_to_buy]), 2)

    @staticmethod
    def print_recipe(recipe_data: list[tuple], customer_name: str,
                     total_cost: float) -> None:
        recipe_header = (f"Date: 04/01/2021 12:33:41\n"
                         f"Thanks, {customer_name}, for your purchase!\n"
                         f"You have bought:")

        print(recipe_header)

        for product in recipe_data:
            print(f"{product[0]} {product[1]}s for "
                  + f"""{round(product[2])
            if product[2] % 1 == 0 else product[2]}"""
                  + " dollars")

        recipe_footer = (
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
        print(recipe_footer)

    def make_purchase(self, product_cart: dict, customer_name: str) -> float:
        cost = 0
        recipe_data = []

        for product_name in product_cart:
            product_cost = round(self.price_list[product_name]
                                 * product_cart[product_name], 2)
            cost += product_cost
            recipe_data.append((product_cart[product_name],
                                product_name, product_cost))

        Shop.print_recipe(recipe_data, customer_name, cost)

        return cost
