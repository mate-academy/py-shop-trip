from app.customer import customers
from app.shop import shops
from app.trip_cost import calculate_trip_cost


def shop_trip() -> None:

    calculate_trip_cost(customers, shops)


if __name__ == "__main__":
    shop_trip()
