import datetime


class Shop:
    def __init__(self,
                 name: str,
                 product_prices: dict,
                 location: list,
                 ) -> None:
        self.name = name
        self.product_prices = product_prices
        self.location = location

    def get_price_for_shoping_cart(self, shoping_cart: dict) -> float:
        amound_of_milk = shoping_cart["milk"]
        amound_of_bread = shoping_cart["bread"]
        amound_of_butter = shoping_cart["butter"]
        return (amound_of_milk * self.product_prices["milk"]
                + amound_of_bread * self.product_prices["bread"]
                + amound_of_butter * self.product_prices["butter"])

    def return_receipt(self, customer_name: str, shoping_cart: dict) -> None:
        formated_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = self.get_price_for_shoping_cart(shoping_cart)
        print(f"Date: {formated_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product_name in shoping_cart.keys():
            product_price = (shoping_cart[product_name]
                             * self.product_prices[product_name])
            if product_price % 1 == 0:
                product_price = int(product_price)
            print(f"{shoping_cart[product_name]} {product_name}s"
                  f" for {product_price} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
