from app.shop_trip_moduls.Cars import Car
from app.shop_trip_moduls.Customers import Customer
from app.shop_trip_moduls.Locations import Point
from app.shop_trip_moduls.Shops import Shop


def create_data_shops(data: dict) -> list:
    return [
        Shop(
            shop["name"],
            Point(shop["location"][0], shop["location"][1]),
            shop["products"]
        ) for shop in data.get("shops")
    ]


def create_data_customers(data: dict) -> list:
    return [
        Customer(
            customer["name"],
            customer["product_cart"],
            Point(customer["location"][0], customer["location"][1]),
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
                data.get("FUEL_PRICE")
            )
        ) for customer in data.get("customers")
    ]


def play_shop_trip(
        list_data_shops: list,
        list_data_customers: list
) -> None:
    for customer in list_data_customers:
        the_cheapest_option = 100000000
        print(f"{customer.name} has {customer.money} dollars")
        best_store = ""
        purchase_price = 0
        for shop in list_data_shops:
            distance = calculate_distance(
                customer.location,
                shop.get_location()
            )
            price_trip = calculate_price_trip(
                customer.car,
                distance
            )
            full_price = count_full_price(
                price_trip,
                shop.price_list,
                customer.product_cart
            )
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {full_price}")
            if full_price < the_cheapest_option:
                the_cheapest_option = full_price
                best_store = shop
        customer.money = customer.money - the_cheapest_option
        if customer.money < 0:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {best_store.name}\n")
        print("Date: 04/01/2021 12:33:41")
        customer_home_location = customer.location
        customer.location = best_store.get_location()
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        for product in best_store.price_list.keys():
            price_for_one_type = (
                customer.product_cart[product]
                * best_store.price_list[product]
            )
            print(
                f"{customer.product_cart[product]} "
                f"{product}s for "
                f"{price_for_one_type} dollars"
            )
            purchase_price += price_for_one_type
        print(f"Total cost is {purchase_price} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        customer.location = customer_home_location
        print(f"{customer.name} now has {customer.money} dollars\n")


def calculate_distance(
        location1: Point,
        location2: Point
) -> float:
    return (
        (
            (
                location1.coord_x
                - location2.coord_x
            ) ** 2
            + (
                location1.coord_y
                - location2.coord_y
            ) ** 2
        ) ** 0.5)


def calculate_price_trip(
        car: Car,
        distance: float
) -> float:
    return round(
        2 * car.fuel_price
        * car.fuel_consumption
        * distance / 100, 2
    )


def count_full_price(
        price_trip: float,
        price_list: dict,
        product_cart: dict
) -> float:
    purchase_price = 0
    for product in price_list.keys():
        if product in product_cart.keys():
            purchase_price += (
                price_list[product]
                * product_cart[product]
            )
    return price_trip + purchase_price
