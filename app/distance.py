from app.customer import Customer


class Distance:
    def __init__(self, customer: Customer, shop: list) -> None:
        self.car_loc = customer.location
        self.shop_loc = shop
        self.customer = customer

    def distance_between(self) -> float:
        x_ = (self.car_loc[0] - self.shop_loc[0])**2
        y_ = (self.car_loc[1] - self.shop_loc[1])**2
        return round(self.customer.full_price
                     * ((((x_ + y_) ** 0.5 * 2)
                         * self.customer.car.fuel_consumption) / 100), 2)
