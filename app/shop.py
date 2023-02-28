def unpack_shops(data: list) -> list:
    list_shops = []
    for shop in data:
        list_shops.append(Shop(shop))
    return list_shops


class Shop:
    def __init__(self, shop):
        self.name = shop["name"]
        self.products = shop["products"]
        self.location = shop["location"]

    def recipe(self, customer):
        total_price = 0
        print(
            f"Date: 04/01/2021 12:33:41\nThanks, "
            f"{customer.name}, for you purchase!\nYou have bought: "
        )
        for k, v in customer.product_cart.items():
            print(f"{v} {k}s for {v * self.products[k]} dollars")
            total_price += v * self.products[k]
        print(f"Total cost is {total_price} dollars\nSee you again!\n")
