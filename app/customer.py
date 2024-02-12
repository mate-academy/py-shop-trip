from math import sqrt
import datetime
class Customer:

    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def calculate_distance(location1, location2):
        distance = sqrt((location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2)
        return round(distance, 2)
        # return distance

    def purchase_receipt(self, shop_name, products):
        current_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nDate: {current_time}\nThanks, {self.name}, for your purchase at {shop_name}!\nYou have bought:")

        total_cost = 0
        for item, quantity in self.product_cart.items():
            cost = products[item] * quantity
            total_cost += round(cost, 2)
            print(f"{quantity} {item}s for {round(cost, 2)} dollars")

        print(f"Total cost is {total_cost:.2f} dollars\nSee you again!")
