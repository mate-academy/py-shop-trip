from app.info import get_information


class Customer:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)
        self.car_fuel_consumption_per_km = self.car["fuel_consumption"] / 100


def create_class_instance_customers_list() -> list:
    customers_list = get_information()["customers"]
    customer_class_list = []
    for customer in customers_list:
        customer_class_list.append(Customer(customer))
    return customer_class_list


def make_rest_of_prints(customer: Customer, cheapest_shop: dict) -> None:
    if customer.money < cheapest_shop["cost"]:
        print(f"{customer.name} doesn't have "
              f"enough money to make purchase in any shop")
    else:
        print(f"{customer.name} rides to {cheapest_shop['name']}")
        customer_home_location = customer.location
        customer.location = cheapest_shop["location"]

        print("\nDate: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        print(f"{customer.product_cart['milk']} milks "
              f"for {cheapest_shop['milk']} dollars")
        print(f"{customer.product_cart['bread']} breads "
              f"for {cheapest_shop['bread']} dollars")
        print(f"{customer.product_cart['butter']} butters "
              f"for {cheapest_shop['butter']} dollars")
        print(f"Total cost is {cheapest_shop['products']} dollars")
        print("See you again!")

        print(f"\n{customer.name} rides home")
        customer.location = customer_home_location

        money_left = customer.money - cheapest_shop["final_cost"]

        print(f"{customer.name} now has {money_left} dollars\n")
