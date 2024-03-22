from datetime import datetime


class Shop:
    def __init__(self, name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_purchase_receipt(self, customer: object) -> None:
        product_sum = 0
        now = datetime.strptime("04/01/2021 12:33:41", "%d/%m/%Y %H:%M:%S")
        print(f"""Date: {now.strftime("%d/%m/%Y %H:%M:%S")}""")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product in customer.products:
            result = (self.products[product]
                      * customer.products[product])

            product_sum += result
            prices = self.products[product] * customer.products[product]
            if isinstance(prices, float):
                prices_str = str(prices)
                prices = prices_str.rstrip("0").rstrip(".")
            print(f"{customer.products[product]} "
                  f"{product}s for {prices} dollars")

        print(f"Total cost is {product_sum} dollars\n" "See you again!\n")
        print(f"{customer.name} rides home")
