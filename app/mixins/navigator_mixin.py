import math


class NavigatorMixin:
    @staticmethod
    def calculate_distance(
            start_point: list[int],
            end_point: list[int]
    ) -> int | float:
        return math.sqrt(
            (end_point[0] - start_point[0]) ** 2
            + (end_point[1] - start_point[1]) ** 2
        )
