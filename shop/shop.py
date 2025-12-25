import datetime


class Shop:
    def __init__(self, fields: dict):
        self.name = fields["name"]
        self.location = fields["location"]
        self.products = fields["products"]

    def print_a_bill(self, customer, fuel_price: float):
        shopping = customer.cost_shopping_trip(self, fuel_price)
        customer.money -= shopping[1]
        date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        bill_header = f"Date: {date}\nThanks, {customer.name}," \
                      f" for you purchase!\nYou have bought: \n"
        product_list = "\n".join(
            f"{count} {product}s for {self.products[product] * count} dollars"
            for product, count in customer.product_cart.items())
        bill_footer = f"\nTotal cost is {shopping[2]}" \
                      f" dollars\nSee you again!\n"

        return bill_header + product_list + bill_footer
