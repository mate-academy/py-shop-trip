from app.shop import Shop
from app.customer import Customer


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_price_road(self, shop: Shop, customer: Customer,
                             fuel_price: float) -> int | float:
        shop_x = shop.location[0]
        shop_y = shop.location[1]
        cust_x = customer.location[0]
        cust_y = customer.location[1]

        len_x = shop_x - cust_x
        len_y = shop_y - cust_y

        road_len = (len_x ** 2 + len_y ** 2) ** 0.5

        consumption_to_shop = self.fuel_consumption / 100 * road_len
        price_of_road = consumption_to_shop * fuel_price * 2
        purchase_price = sum(shop.products[product] * pieces
                             for product, pieces
                             in customer.products_cart.items())
        price_of_trip = round(price_of_road + purchase_price, 2)
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {price_of_trip}")
        return price_of_trip
