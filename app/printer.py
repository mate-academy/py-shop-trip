from app.shop import Shop
from datetime import datetime
from app.customer import Customer


class Printer:

    @staticmethod
    def print_info(
            receipt: list,
            all_cost: list,
            shops_cost: list,
            customer: Customer
    ) -> None:

        cheapest_store_index = all_cost.index(min(all_cost))

        cheapest_store = Shop.shops[
            cheapest_store_index
        ].name

        receipt_date = datetime(2021, 1, 4, 12, 33, 41)

        date = receipt_date.strftime("%d/%m/%Y %H:%M:%S")

        print(f"{customer.name} has {customer.money} dollars")
        for index, shop in enumerate(Shop.shops):
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {all_cost[index]}")
        if customer.money < all_cost[cheapest_store_index]:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_store}")
            print("")
            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for line in receipt[cheapest_store_index]:
                print(line)
            print(f"Total cost is {shops_cost[cheapest_store_index]} dollars")
            print("See you again!")
            print("")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - all_cost[cheapest_store_index]} dollars")
            print("")
