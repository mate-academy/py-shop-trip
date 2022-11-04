import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_check(self, customer: any) -> None:
        data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
        print(f"Date: {data}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, amount in customer.product_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price} dollars")
        print(f"Total cost is {customer.product_price(self).get(self.name)}"
              f" dollars")
        print("See you again!")
