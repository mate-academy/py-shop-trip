from app.customer import Customer
from app.shop import Shop
from app.logic_funcs import counting_product_price, counting_trips, info


def shop_trip() -> None:
    customers = [Customer(**customer) for customer in info["customers"]]
    shops = {market["name"]: Shop(**market) for market in info["shops"]}

    for person in customers:
        counted_trip = counting_trips(person, shops)

        if min(counted_trip) > person.money:
            print(
                f"{person.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
        else:
            cheapest_shop = counted_trip[min(counted_trip)]
            person.ride_to_shop(cheapest_shop)
            counting_product_price(person, shops, cheapest_shop)
            person.ride_to_home(price=min(counted_trip))


shop_trip()
