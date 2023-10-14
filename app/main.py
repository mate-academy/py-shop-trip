from app.car import Roads
from app.customer import persons


def shop_trip() -> None:
    road = Roads()
    for person in persons:
        road.find_chip_market(person)
        if road.min_cost >= person.money:
            continue
        print()
        road.count_customer_check(person)
        print()
        road.fuel_cost_get_at_home(person)
        print()


shop_trip()
