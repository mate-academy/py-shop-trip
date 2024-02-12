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
        total_cost = self.get_price_for_shoping_cart(shoping_cart)
        milk_price = shoping_cart["milk"] * self.product_prices["milk"]
        bread_price = int(shoping_cart["bread"] * self.product_prices["bread"])
        butter_price = shoping_cart["butter"] * self.product_prices["butter"]
        receipt = f"""
Date: 04/01/2021 12:33:41
Thanks, {customer_name}, for your purchase!
You have bought:
{shoping_cart["milk"]} milks for {milk_price} dollars
{shoping_cart["bread"]} breads for {bread_price} dollars
{shoping_cart["butter"]} butters for {butter_price} dollars
Total cost is {total_cost} dollars
See you again!\n"""
        print(receipt)
