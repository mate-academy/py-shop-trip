import datetime


class Shop:
    def __init__(self, name: str, location: list[int, int], products: dict):
        self.name = name
        self.location_x = location[0]
        self.location_y = location[1]
        self.products = products

    def calculate_product_price(self, product_name: str, number: int):
        if product_name in self.products:
            return number * self.products[product_name]
        else:
            print(f"Sorry, we don't have {product_name}")
            return None

    def give_check(self, customer_name: str, product_cart: dict):
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        result = 0.0
        print(f"Date: {current_date}\n"
              f"Thanks, {customer_name}, for you purchase!\n"
              f"You have bought: ")

        for product, number in product_cart.items():
            product_price = self.calculate_product_price(product, number)
            if product_price is not None:
                print(f"{number} {product}s for {product_price} dollars")
                result += product_price

        print(f"Total cost is {result} dollars\n"
              f"See you again!\n")
        return result
