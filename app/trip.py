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
            specific_shop_trip_price = Trip.calculate_costs(
                customer, shop, fuel_price
            )
            trip_prices[specific_shop_trip_price] = shop

            print(
                (f"{customer.name}'s trip to the {shop.name} "
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
                f"You have bought: \n"
                f"{milk_amount} milks for "
                f"{milk_amount * milk_price} dollars\n"
                f"{bread_amount} breads for "
                f"{bread_amount * bread_price} dollars\n"
                f"{butter_amount} butters for "
                f"{butter_amount * butter_price} dollars\n"
                f"Total cost is {total_cost} dollars\n"
                f"See you again!\n"
                f"\n")

    @staticmethod
    def get_money(customer: Customer) -> str:
        return f"{customer.name} has {customer.money} dollars"

    @staticmethod
    def distance_between_shop_and_customer(
            customer: Customer,
            shop: Shop
    ) -> int:

        x_axis = (
            (shop.location[0] - customer.location[0]) ** 2
        )
        y_axis = (
            (shop.location[1] - customer.location[1]) ** 2
        )
        return (x_axis + y_axis) ** 0.5

    @staticmethod
    def products_cost(
            customer: Customer,
            shop: Shop,
    ) -> float:

        return sum([
            amount * price
            for amount, price in
            zip(customer.product_cart.values(), shop.products.values())])

    @staticmethod
    def calculate_costs(
            customer: Customer,
            shop: Shop,
            fuel_price: float
    ) -> float:

        distance = Trip.distance_between_shop_and_customer(
            customer, shop
        )
        consumption = customer.car["fuel_consumption"] / 100 * distance

        fuel_consumption_cost = consumption * fuel_price * 2

        return round(
            fuel_consumption_cost + Trip.products_cost(customer, shop)
            , 2)
