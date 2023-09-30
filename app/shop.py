import datetime


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]

    def print_purchase_receipt(self,
                               product_cart: dict,
                               customer_name: str) -> None:
        date = datetime.datetime.now()
        format_date = date.strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nDate: {format_date}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought: ")

        total_cost = 0
        for product in product_cart:
            quantity = product_cart[product]
            cost = self.products[product] * quantity
            total_cost += cost
            print(f"{quantity} {product if quantity < 1 else product+'s'} "
                  f"for {cost if cost % 1 != 0 else int(cost)} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!")
