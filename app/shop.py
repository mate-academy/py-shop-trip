import datetime


class Shop:
    def __init__(self,
                 name,
                 location,
                 products,
                 ):
        self.name = name
        self.location = location
        self.products = products
        self.receipt = None
        self.total_cost = 0

    def shopping(self, customer):
        total_to_pay = 0
        item_details = ""
        for key in self.products:
            item_total = self.products[key] * customer.product_cart[key]
            total_to_pay += item_total
            item_details += f"{customer.product_cart[key]} {key}s" \
                            f" for {item_total} dollars\n"
        date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.receipt = f"Date: {date}\n" \
                       f"Thanks, {customer.name}, for you purchase!\n" \
                       f"You have bought: \n" \
                       f"{item_details}" \
                       f"Total cost is {total_to_pay} dollars\n" \
                       f"See you again!"
        total_amount = round(total_to_pay, 2)
        return total_amount

    def distance_to_shop(self, customer, fuel_price):
        customer_x = customer.location[0]
        customer_y = customer.location[1]
        shop_x = self.location[0]
        shop_y = self.location[1]
        km = ((customer_x - shop_x) ** 2 + (customer_y - shop_y) ** 2) ** 0.5
        fuel_expenses = km / 100 * customer.fuel_consumption * fuel_price * 2
        return round(fuel_expenses, 2)

    def cost_of_trip(self, customer, fuel_price):
        travel_cost = self.distance_to_shop(customer, fuel_price)
        shopping_cost = self.shopping(customer)
        self.total_cost = travel_cost + shopping_cost
        return self.total_cost
