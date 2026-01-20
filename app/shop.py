from datetime import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def _get_cost(product_price, quantity) -> float:
        return product_price * quantity

    def get_total_cost(self, product_list) -> float:
        total_cost = 0
        for product, quantity in product_list.items():
            total_cost += Shop._get_cost(self.products[product], quantity)
        return total_cost

    def get_receipt(self,
                    customer_order: dict,
                    customer_name: str) -> str:
        receipt_str = ""
        datetime_obj = datetime.now()
        receipt_str += datetime_obj.strftime("Date: %d/%m/%Y %H:%M:%S\n")
        receipt_str += f"Thanks, {customer_name}, for your purchase!\n"
        receipt_str += "You have bought:\n"
        for product, quantity in customer_order.items():
            product_name = product
            if customer_order[product] > 1:
                product_name += "s"
            receipt_str += f"{quantity} {product_name} for " \
                           f"{Shop._get_cost(self.products[product], quantity)} " \
                           f"dollars \n"
        receipt_str += f"Total cost is {self.get_total_cost(customer_order)} dollars\n"
        receipt_str += "See you again!\n"
        return receipt_str


# Date: 04/01/2021 12:33:41
# Thanks, Bob, for your purchase!
# You have bought:
# 4 milks for 12 dollars
# 2 breads for 2 dollars
# 5 butters for 12.5 dollars
# Total cost is 26.5 dollars
# See you again!