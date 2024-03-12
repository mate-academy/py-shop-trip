def calculate_distance(
        location1: tuple[float, float],
        location2: tuple[float, float]
) -> float:
    dx = location1[0] - location2[0]
    dy = location1[1] - location2[1]
    return (dx ** 2 + dy ** 2) ** 0.5
