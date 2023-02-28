from app.customer import Customer


def unpack_shops(data: list) -> list:
    list_shops = []
    for shop in data:
        list_shops.append(Shop(shop))
    return list_shops


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.products = shop["products"]
        self.location = shop["location"]

    def recipe(self, customer: Customer) -> None:
        total_price = 0
        print(
            f"Date: 04/01/2021 12:33:41\nThanks, "
            f"{customer.name}, for you purchase!\nYou have bought: "
        )
        for name, value in customer.product_cart.items():
            print(f"{value} {name}s for {value * self.products[name]} dollars")
            total_price += value * self.products[name]
        print(f"Total cost is {total_price} dollars\nSee you again!\n")
