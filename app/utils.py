import os
import json
import math
from typing import List, Dict, Any, Union


def load_info(file_name: str) -> Dict[str, Any]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)


def calculate_distance(
        location_1: List[Union[int, float]],
        location_2: List[Union[int, float]]
) -> float:
    x1, y1 = location_1
    x2, y2 = location_2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
