class Shops:
    list_of_shops = []

    def __init__(self, shop_dict: dict) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["products"]
        self.__class__.list_of_shops.append(self)

    def get_total(self, customer: iter) -> float:
        total_cost = sum(
            [customer.prod_cart[key] * self.product[key]
             for key in customer.prod_cart])
        return total_cost

    def print_receipt(self, customer: iter) -> None:
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer.name}, for you purchase!\n"
            f"You have bought: ")
        for key in customer.prod_cart:
            print(
                f"{customer.prod_cart[key]} {key}s for "
                f"{customer.prod_cart[key] * self.product[key]} dollars")
        print(f"Total cost is {self.get_total(customer)} dollars")
        print("See you again!\n")
