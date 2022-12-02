import datetime
from unittest import mock
from app.customer import Customers
from app.shop import Shop, calculation_of_the_cost_of_purchases
from app.car import price_for_fuel


@mock.patch("datetime.datetime.now")
def shop_trip(mocked_time: str) -> None:
    mocked_time.return_value = "04/01/2021 12:33:41"
    Customers.create_customers()
    Shop.create_shops()
    for customer in Customers.list_of_customers:
        print(f"{customer.name} has {customer.money} dollars")
        expenses_shop = {}
        for shop in Shop.list_of_shops:
            fuel = price_for_fuel(customer, shop)
            purchase = calculation_of_the_cost_of_purchases(customer, shop)
            costs = fuel + purchase
            costs = round(costs, 2)
            print(f"{customer.name}'s trip to the {shop.name} costs {costs}")
            expenses_shop[costs] = shop.name
        alternative_costs = []
        for expenses in expenses_shop:
            alternative_costs.append(expenses)
        our_choice = min(alternative_costs)
        if our_choice > customer.money:
            print(f"{customer.name} doesn't have enough money to "
                  f"make purchase in any shop")
        else:
            print(f"{customer.name} rides to {expenses_shop[our_choice]}\n")
            shop_for_trip = None
            for choice_shop in Shop.list_of_shops:
                if choice_shop.name == expenses_shop[our_choice]:
                    shop_for_trip = choice_shop
            home = customer.location
            customer.location = shop_for_trip.location
            print(f"Date: {datetime.datetime.now()}")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            total_cost = 0
            for product, amount in customer.product_cart.items():
                costs = amount * shop_for_trip.products[product]
                print(f"{amount} {product}s for {costs} dollars")
                total_cost += costs
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home
            money = customer.money - our_choice
            print(f"{customer.name} now has {money} dollars\n")
