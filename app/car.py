from __future__ import annotations

import json
import math

from typing import List
from decimal import Decimal


class Car:
    def __init__(self, dictionary: dict) -> None:
        self.brand = dictionary.get("brand")
        self.fuel_consumption = dictionary.get("fuel_consumption")

    def fuel_price_for_distance(
            self,
            start: List[int, int],
            finish: List[int, int]
    ) -> float:
        with open("app/config.json") as config:
            data = json.load(config)
            fuel_price = Decimal(str(data.get("FUEL_PRICE")))
        #  distance = √((хs – хf)2 + (уs – уf)2)
        start_x, start_y = start[0], start[1]
        finish_x, finish_y = finish[0], finish[1]
        distance = Decimal(str(
            math.sqrt((start_x - finish_x) ** 2 + (start_y - finish_y) ** 2)
        ))
        double_distance = distance * 2
        fuel_need_for_one_km = Decimal(str(self.fuel_consumption / 100))
        return round(
            float(fuel_need_for_one_km * double_distance * fuel_price), 2
        )
