import dataclasses
import datetime

# from app.Customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_products(self, customer):
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        total_cost = milk_cost + bread_cost + butter_cost
        return total_cost

    def trip_to_shop(self, customer):
        cost_trip = self.cost_products(customer) + customer.fuel_cost(self) * 2
        return round(cost_trip, 2)

    def purchase_receipt(self, customer):
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        total_cost = milk_cost + bread_cost + butter_cost

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        print(f"{customer.product_cart['milk']} milks for {milk_cost} dollars")
        print(f"{customer.product_cart['bread']} "
              f"breads for {bread_cost} dollars")
        print(f"{customer.product_cart['butter']} "
              f"butters for {butter_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
