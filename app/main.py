from app.car import Road
from app.customer import create_customers


def shop_trip() -> None:
    road = Road()
    for person in create_customers():
        road.find_chip_market(person)
        if road.min_cost >= person.money:
            continue
        road.count_customer_check(person)
        road.fuel_cost_get_at_home(person)


if __name__ == "__main__":
    shop_trip()
