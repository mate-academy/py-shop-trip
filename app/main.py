import datetime

from app.customers import create_customer_objects
from app.shops import create_shops_objects
from app.calculate_cost import calculate_cost_for_customer_for_every_shop


def shop_trip() -> None:
    customers = create_customer_objects()
    shops = create_shops_objects()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = calculate_cost_for_customer_for_every_shop(customer)
        for shop, cost in costs.items():
            print(f"{customer.name}'s trip to the {shop} costs {cost}")
        if customer.money < min(list(costs.values())):
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
            continue
        index = list(costs.values()).index(min(costs.values()))
        shop_to_visit = list(costs.keys())[index]
        print(f"{customer.name} rides to {shop_to_visit}\n")
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}\nThanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for shop in shops:
            if shop.name == shop_to_visit:
                for product, count in customer.product_cart.items():
                    amount = count * shop.products[product]
                    total_cost += amount
                    print(f"{count} {product}s for {amount} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
        moneys_left = customer.money - min(costs.values())
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {moneys_left} dollars\n")
