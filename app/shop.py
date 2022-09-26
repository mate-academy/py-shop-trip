import datetime


class Shop:
    """
    This class creates a store.
    It has one method that prints a receipt with purchases.
    """
    def __init__(self, shop):
        # Create a shop
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def get_cheque(self, client):
        # Prints cheque
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {client.name}, for you purchase!\nYou have bought: ")
        cost_ = 0
        for product in self.products:
            if product in client.product_cart:
                amount = self.products[product] * client.product_cart[product]
                cost_product = f"{client.product_cart[product]} {product}s" \
                               f" for {amount} dollars"
                cost_ += self.products[product] * client.product_cart[product]
                print(cost_product)
        print(f"Total cost is {cost_} dollars\nSee you again!\n")
