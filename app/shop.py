import datetime


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name: str = shop["name"]
        self.location: list = shop["location"]
        self.products: dict = shop["products"]

    def get_product_prices(self, customer_product_cart: dict) -> dict:
        product_prices_for_customer = {}

        for product_name, product_count in customer_product_cart.items():
            if product_name in self.products:
                product_price: float = self.products[product_name]
                product_prices_for_customer[product_name] = {
                    "price_per_unit": product_price,
                    "count": product_count,
                    "total_product_price": product_price * product_count
                }

        total_purchases_price = sum(
            item["count"] * item["price_per_unit"]
            for item in product_prices_for_customer.values()
        )

        return {
            "product_prices": product_prices_for_customer,
            "total_purchases_price": total_purchases_price
        }

    def sell_products(self, customer_name: str, product_cart: dict) -> dict:
        purchase_date_time: str = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        products: dict = self.get_product_prices(product_cart)
        prices_for_customer: dict = products["product_prices"]
        total_cost: float = products["total_purchases_price"]

        def format_price(price: float) -> str:
            formatted_price = "{:.2f}".format(price).rstrip("0").rstrip(".")
            return formatted_price

        def print_receipt() -> None:
            print(
                f"Date: {purchase_date_time}\n"
                f"Thanks, {customer_name}, for your purchase!\n"
                f"You have bought: "
            )

            for product_name, details in prices_for_customer.items():
                purchase_count = details["count"]
                total_price = details["price_per_unit"] * purchase_count
                formatted_price = format_price(total_price)
                print(f"{purchase_count} {product_name}s "
                      f"for {formatted_price} dollars")
            formatted_total_cost = format_price(total_cost)
            print(
                f"Total cost is {formatted_total_cost} dollars\n"
                "See you again!\n"
            )

        print_receipt()
        return products
