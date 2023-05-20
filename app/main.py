from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    customers = Customer.create_customers()
    shops = Shop.create_shops()
    for customer in customers:
        cheapest_shop = Shop.find_cheapest_shop(shops, customer)
        cheapest_shop_trip = Shop.calculate_shop_trip(
            cheapest_shop, customer
        )[cheapest_shop]
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            shop_trip_cost = Shop.calculate_shop_trip(shop, customer)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {shop_trip_cost[shop]}")
        if customer.money < cheapest_shop_trip:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        Shop.generate_receipt(cheapest_shop, customer)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{round(customer.money - cheapest_shop_trip, 2)} "
              f"dollars\n")
