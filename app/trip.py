import datetime
from app.shop import Shop
from app.customer import Customer


class Trip:

    @staticmethod
    def choosing_the_cheapest_shop(
            customer: Customer,
            shops: list[Shop],
            fuel_price: float
    ) -> Shop or None:
        trip_prices = {}
        for shop in shops:
            specific_shop_trip_price = Trip.calculate_cost_of_ride_to_shop(
                customer, shop, fuel_price
            )
            trip_prices[specific_shop_trip_price] = shop

            print(
                (f"{customer.name}`s trip to the {shop.name} "
                 f"costs {specific_shop_trip_price}")
            )
        lowest_trip_cost = min(trip_prices)
        if customer.money >= lowest_trip_cost:
            return trip_prices[lowest_trip_cost]

    @staticmethod
    def shopping(shop: Shop, customer: Customer) -> str:
        milk_amount, milk_price = (customer.product_cart["milk"],
                                   shop.products["milk"])
        bread_amount, bread_price = (customer.product_cart["bread"],
                                     shop.products["bread"])
        butter_amount, butter_price = (customer.product_cart["butter"],
                                       shop.products["butter"])
        total_cost = ((milk_amount * milk_price)
                      + (bread_amount * bread_price)
                      + (butter_amount * butter_price))

        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return (f"Date: {date}\n"
                f"Thanks, {customer.name}, for you purchase!\n"
                f"You have bought:\n"
                f"{milk_amount} milks for"
                f"{milk_amount * milk_price} dollars\n"
                f"{bread_amount} breads for"
                f"{bread_amount * bread_price} dollars\n"
                f"{butter_amount} butters for "
                f"{butter_amount * butter_price} dollars\n"
                f"Total cost is {total_cost} dollars\n"
                f"See you again!\n"
                f"\n"
                f"{customer.name} rides home\n"
                f"{customer.name} now has "
                f"{customer.money - total_cost} dollars\n")

    @staticmethod
    def get_money(customer: Customer) -> str:
        return f"{customer.name} has {customer.money} dollars"

    @staticmethod
    def calculate_distance_between_shop_and_customer(
            customer: Customer,
            shop: Shop
    ) -> int:

        customer_location = (
            (customer.location[0] - customer.location[1]) ** 2
        )
        shop_location = (
            (shop.location[0] - shop.location[1]) ** 2
        )
        return (customer_location + shop_location) ** 0.5

    @staticmethod
    def calculate_cost_of_ride_to_shop(
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> float:

        distance = Trip.calculate_distance_between_shop_and_customer(
            customer, shop
        )

        trip_cost = round(
            (distance / customer.car["fuel_consumption"]) * fuel_price
        )
        return trip_cost
