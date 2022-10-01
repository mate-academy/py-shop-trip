from datetime import datetime

from app.shop import shops
from app.customer import customers


def shop_trip():
    current = datetime.now()
    current = current.strftime("%d/%m/%y %H:%M:%S")

    min_ = 1000000
    market = None
    cost = 0
    total_cost = 0
    for human in customers:
        print(f"{human.name} has {human.money} dollars")
        for store in shops:
            print(f"{human.name}`s trip to the {store.name} "
                  f"coasts {store.calculate_trip(human)}")
            if store.calculate_trip(human) < min_:
                min_ = store.calculate_trip(human)
        if human.money > min_:
            for store in shops:
                if store.calculate_trip(human) == min_:
                    market = store
                    print(f"{human.name} rides to {store.name}\n")
            print(f"Date: {current}")
            print(f"Thanks, {human.name}, for you purchase!")
            print("You have bought: ")
            for prod, amt in human.product_cart.items():
                for product, price in market.products.items():
                    if prod == product:
                        cost = amt * price
                        total_cost += cost
                print(f"{amt} {prod} for {cost} dollars")
                cost = 0
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")
            print(f"{human.name} rides home")
            print(f"Bob now has "
                  f"{human.money - market.calculate_trip(human)}"
                  f" dollars\n")
        else:
            print(f"{human.name} doesn't have enough "
                  f"money to make purchase in any shop")


shop_trip()
