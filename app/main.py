import json
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers, fuel_price, shops = get_data()
    for customer in customers:
        head_report = f"{customer.name} has {customer.money} dollars"
        maxima, choice, bill = float("inf"), 0, 0,
        for shop in shops:
            buy_coast, check = shop.purchase_cost_for(customer)
            if buy_coast:
                buy_coast = round(buy_coast, 2)
                trip_coast = buy_coast + customer.car.fuel_cost(
                    customer.distance_to(shop), fuel_price)
                head_report += (f"\n{customer.name}'s "
                                f"trip to the {shop.name} costs {trip_coast}")
                if maxima > trip_coast <= customer.money:
                    maxima, choice, bill = trip_coast, shop, check
        print(head_report)
        finish_report(bill, choice, customer, maxima)


def finish_report(bill: str,
                  choice: Shop,
                  customer: Customer,
                  maxima: float | int,
                  ) -> None:
    if choice:
        date_stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        customer.money -= maxima
        print(f"{customer.name} rides to {choice.name}\n"
              f"\nDate: {date_stamp}"
              f"\nThanks, {customer.name}, for your purchase!"
              "\nYou have bought:"
              f"\n{bill}"
              f"\nSee you again!\n"
              f"\n{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")
    else:
        print(f"{customer.name} doesn't have enough money "
              "to make a purchase in any shop")


def get_data() -> tuple[list[Customer], float, list[Shop]]:
    with open("app/config.json") as file:
        data = json.load(file)
        (_, fuel_price), (_, customers), (_, shops) = data.items()
    return ([Customer(**customer) for customer in customers],
            fuel_price,
            [Shop(**shop) for shop in shops])


if __name__ == "__main__":
    shop_trip()
