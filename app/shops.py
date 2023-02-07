from datetime import datetime


class Shops:
    list_of_shops = []

    def __init__(self, shop_dict) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["products"]
        self.__class__.list_of_shops.append(self)

    def get_total(self, customer) -> float:
        total_cost = sum(
            [customer.prod_cart[key] * self.product[key]
             for key in customer.prod_cart])
        return round(total_cost, 2)

    def print_receipt(self, customer) -> None:
        print(
            f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for you purchase! in {self.name} \n"
            f"You have bought:")
        for key in customer.prod_cart:
            print(
                f"{customer.prod_cart[key]} {key} for "
                f"{customer.prod_cart[key] * self.product[key]} dollars")
        print(f"Total cost is {self.get_total(customer)} dollars")
        print("See you again!\n")




