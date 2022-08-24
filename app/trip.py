from app.customer import Customer
from app.shop import Shop


class Trip:
    def __init__(self, customer: Customer, shop: Shop, fuel_price: float):
        self.customer = customer
        self.shop = shop

        self._cost_of_fuel = self._calc_fuel() * fuel_price
        self._cost_of_cart = self._calc_cart()

    @property
    def cost_of_trip(self) -> float:
        return round(self._cost_of_fuel + self._cost_of_cart, 2)

    @property
    def cost_of_cart(self) -> float:
        return self._cost_of_cart

    @property
    def cash_bill(self) -> dict:
        return {
            f"{self.customer.product_cart[item]} {item}s":
                self.customer.product_cart[item] * self.shop.get_price(item)
            for item
            in self.customer.product_cart
        }

    @property
    def cash_rest(self) -> float:
        return round(self.customer.money - self.cost_of_trip, 2)

    def _calc_fuel(self) -> float:
        distance = self.customer.location.calc_distance(self.shop.location)
        return 2 * self.customer.car.calc_fuel_consumption(distance)

    def _calc_cart(self) -> float:
        return sum(
            self.customer.product_cart[item] * self.shop.get_price(item)
            for item
            in self.customer.product_cart
        )
