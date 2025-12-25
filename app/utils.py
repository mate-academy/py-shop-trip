def calculate_distance(location1: list, location2: list) -> float:
    x1, y1 = location1
    x2, y2 = location2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
