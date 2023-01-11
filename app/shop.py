class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_of_all_products(self, product_cart: dict) -> int:
        cost = 0
        for product, amount in product_cart.items():
            cost += amount * self.products[product]
        return cost

    def shopping(self, person: object) -> None:
        print(f"{person.name} rides to {self.name}\n")
        person.location = self.location
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {person.name}, for you purchase!\n"
              "You have bought: ")

        for item, amount in person.product_cart.items():
            cost_of_product = amount * self.products[item]
            print(f"{amount} {item}s for {cost_of_product} dollars")

        print(f"Total cost is "
              f"{self.cost_of_all_products(person.product_cart)} dollars\n"
              f"See you again!\n")
