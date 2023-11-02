class Shop:
    shops = []

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops.append(self)

    def __repr__(self) -> str:
        return self.name

    def print_bill(self, customer_name: str, product_cart: dict) -> None:
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              "You have bought: ")
        total_cost = 0
        for product in product_cart:
            cost = product_cart[product] * self.products[product]
            if cost == int(cost):
                cost = int(cost)
            total_cost += cost
            print(f"{product_cart[product]} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              "See you again!\n")
