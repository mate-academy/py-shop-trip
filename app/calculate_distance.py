def calculate_distance(location1: list, location2: list) -> list:
    x1, y1 = location1
    x2, y2 = location2

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance
