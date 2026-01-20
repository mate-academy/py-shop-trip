import datetime


class Shop:
    shop_list: list["Shop"] = []

    def __init__(self, **data) -> None:
        self.name = data.get("name")
        self.location = data.get("location")
        self.products = data.get("products")

    @classmethod
    def generate_shop(cls, data: dict) -> None:
        for shop in data["shops"]:
            store = Shop(**shop)
            cls.shop_list.append(store)

    def get_service(self, customer: any) -> float:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        products_sum_price = 0
        sales_details = []
        for product, count in customer.product_cart.items():
            price = self.products.get(product)
            total_product_cost = price * count
            products_sum_price += total_product_cost

            sales_details.append(
                f"{count} {product}s "
                f"for {self.format_amount(total_product_cost)} dollars")

        print(f"\nDate: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for detail in sales_details:
            print(f"{detail}")
        print(f"Total cost is {round(products_sum_price, 2)} dollars")
        print("See you again!\n")
        return products_sum_price

    @staticmethod
    def format_amount(amount: float) -> str:
        amount_str = "{:.2f}".format(amount).rstrip("0").rstrip(".")

        return amount_str
