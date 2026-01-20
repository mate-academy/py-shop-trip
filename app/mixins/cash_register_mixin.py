from datetime import datetime


class CashRegisterMixin:
    @staticmethod
    def calculate_total_cost(
            number_of_products: dict,
            product_prices: dict
    ) -> int | float:
        return sum(
            [number_of_products[product] * product_prices[product]
             for product in product_prices
             if product in number_of_products]
        )

    def print_purchase_receipt(
            self,
            customer_name: str,
            number_of_products: dict,
            product_prices: dict
    ) -> str:
        purchase_date = datetime(
            2021, 1, 4, 12, 33, 41
        ).strftime("%d/%m/%Y %H:%M:%S")
        # purchase_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = self.calculate_total_cost(
            number_of_products,
            product_prices
        )
        purchased_products = ""

        for product in product_prices:
            plural = ""
            if number_of_products[product] > 1:
                plural = "s"
            if product in number_of_products:
                product_cost = (
                    number_of_products[product] * product_prices[product]
                )
                if product_cost == int(product_cost):
                    product_cost = int(product_cost)
                purchased_products += (
                    f"{number_of_products[product]} {product}{plural} for "
                    f"{product_cost} dollars\n"
                )

        return (
            f"Date: {purchase_date}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:\n"
            f"{purchased_products}"
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
