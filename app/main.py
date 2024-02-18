import json
from app.car import CarClass
from app.customer import CustomerClass
from app.shop import ShopClass


def shop_trip() -> None:
    with open("app/config.json", "rb") as file:
        data = json.load(file)
        CarClass.FUEL_PRICE = data["FUEL_PRICE"]
        customers = [CustomerClass(customer) for customer in data["customers"]]
        shops = [ShopClass(shop) for shop in data["shops"]]

        for customer in customers:

            # The first block of text
            print(f"{customer.name} has {customer.money} dollars")
            all_calculations = []
            for shop in shops:
                calculation = customer.shopping(shop)
                all_calculations.append(calculation)
                print(f"{customer.name}'s trip to the {calculation.name.name} "
                      f"costs {calculation.whole_trip_cost}")
            cheapest_trip = min(
                all_calculations, key=lambda trip: trip.whole_trip_cost
            )
            if customer.money < cheapest_trip.whole_trip_cost:
                print(f"{customer.name} doesn't have enough "
                      f"money to make a purchase in any shop")
                break
            print(f"{customer.name} rides to {cheapest_trip.name.name}\n")
            customner_home_location = customer.location
            customer.location = cheapest_trip.name.location

            # The second block of text
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for transaction in cheapest_trip.transactions_list:
                print(transaction)
            print(f"Total cost is {cheapest_trip.total} dollars")
            customer.money -= cheapest_trip.whole_trip_cost
            print("See you again!\n")

            # The third block of text
            print(f"{customer.name} rides home")
            customer.location = customner_home_location
            print(f"{customer.name} now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
