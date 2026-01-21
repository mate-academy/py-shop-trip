from app.parsers import parse_shops, parse_customers, parse_fuel_price
from app.calculations import calculate_trip_cost


def shop_trip() -> None:
    customers = parse_customers()
    shops = parse_shops()
    fuel_price = parse_fuel_price()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_option = None
        for shop in shops:
            trip_cost = calculate_trip_cost(
                customer,
                shop,
                fuel_price,
                customer.car
            )
            if not cheapest_option or cheapest_option[0] > trip_cost:
                cheapest_option = (trip_cost, shop)
            print(f"{customer.name}'s trip to"
                  f" the {shop.name} costs {trip_cost}")
        if cheapest_option[0] > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest_option[1].name}")
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total = 0
        for item in customer.products_to_buy:
            total_price_for_item = (cheapest_option[1].available_products[item]
                                    * customer.products_to_buy[item])
            total_price_for_item = int(total_price_for_item) \
                if float(total_price_for_item).is_integer() \
                else total_price_for_item
            total += round(total_price_for_item, 2)
            print(f"{customer.products_to_buy[item]} {item}s "
                  f"for {total_price_for_item} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        customer.money -= cheapest_option[0]
        print(f"{customer.name} now has{customer.money: .2f} dollars")
        print()
