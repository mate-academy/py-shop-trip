from math import sqrt


class Location:
    @staticmethod
    def calculate_distance(
            shop_location: list[int],
            customer_location: list[int]
    ) -> float:
        return sqrt((shop_location[0] - customer_location[0]) ** 2
                    + (shop_location[1] - customer_location[1]) ** 2)
