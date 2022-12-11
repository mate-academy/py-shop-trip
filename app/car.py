from math import sqrt


def distance(first_location: list, second_location: list) -> float:
    x1 = first_location[0]
    y1 = first_location[1]
    x2 = second_location[0]
    y2 = second_location[1]

    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
