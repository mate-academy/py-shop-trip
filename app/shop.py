import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def receipt_for_products(self, customer_list: dict) -> float:
        total_amount = 0
        for product, quantity in customer_list.items():
            price_for_product = self.products.get(product, 0) * quantity
            total_amount += price_for_product
        return total_amount

    def print_receipt(self, customer_list: dict, customer_name: str) -> None:
        formatted_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nDate: {formatted_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, times in customer_list.items():
            price_for_products = self.products[product] * times
            product_name = product + "s" if times > 1 else product
            if price_for_products == int(price_for_products):
                print(
                    f"{times} {product_name} "
                    f"for {int(price_for_products)} dollars"
                )
            else:
                print(
                    f"{times} {product_name} "
                    f"for {price_for_products} dollars"
                )

        total_amount = self.receipt_for_products(customer_list)
        print(f"Total cost is {total_amount} dollars")
        print("See you again!")
        print()
