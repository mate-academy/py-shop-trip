import datetime


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]
        self.today_date = datetime.datetime(2021, 4, 1, 12, 33, 41)

    def buy_products(self, name: str, customer_products: dict) -> None:
        print(f"Date: {self.today_date.strftime('%m/%d/%Y %H:%M:%S')}\n"
              f"Thanks, {name}, for your purchase!\n"
              f"You have bought:")

        total_cost = 0
        for product, pieces in customer_products.items():
            if product in self.products:
                product_name = product
                if pieces > 1:
                    product_name += "s"
                price = self.products[product] * pieces
                if price.is_integer():
                    price = int(price)
                print(f"{pieces} {product_name} for {price} dollars")
                total_cost += self.products[product] * pieces

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!")
        print()
