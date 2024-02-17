import datetime


class Shop:
    list_of_all_shops = []

    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        self.list_of_all_shops.append(self)

    def total_purchase_cost(self, purchase_list: dict) -> float:
        total_purchase = 0
        for product, quantity in purchase_list.items():
            total_purchase += self.products[product] * quantity
        return total_purchase

    def receipt(self, customer_name: str, purchase_list: dict) -> float:
        total_cost = self.total_purchase_cost(purchase_list)
        print(
            f"Date: {datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:")
        for product, quantity in purchase_list.items():
            buy_product = self.products[product] * quantity
            if buy_product % 1 == 0:
                buy_product = int(buy_product)
            print(
                f"{quantity} {product} for {buy_product} dollars")
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n")
        return round(total_cost, 2)


