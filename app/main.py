import json
import os
from typing import List, Dict, Any

# Читання конфігурації з JSON
config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Дані з конфігу
shops_data: List[Dict[str, Any]] = config["shops"]
customers_data: List[Dict[str, Any]] = config["customers"]
fuel_price: float = config["FUEL_PRICE"]

def calculate_trip_cost(distance_km: float, fuel_price: float, fuel_consumption_per_100km: float = 8.0) -> float:
    """Розрахунок вартості поїздки на основі відстані та ціни пального."""
    liters_needed = (distance_km / 100) * fuel_consumption_per_100km
    return round(liters_needed * fuel_price, 2)

def shop_trip(customer_name: str) -> Dict[str, Any]:
    """Повертає найвигідніший магазин для клієнта з урахуванням вартості поїздки."""
    customer = next((c for c in customers_data if c["name"] == customer_name), None)
    if not customer:
        raise ValueError(f"Клієнт '{customer_name}' не знайдений")

    best_option = None
    lowest_total_cost = float("inf")

    for shop in shops_data:
        product_price = shop["products"].get(customer["product"])
        if product_price is None:
            continue

        trip_cost = calculate_trip_cost(shop["distance_km"], fuel_price)
        total_cost = product_price + trip_cost

        if total_cost < lowest_total_cost:
            lowest_total_cost = total_cost
            best_option = {
                "shop": shop["name"],
                "product_price": round(product_price, 2),
                "trip_cost": trip_cost,
                "total_cost": round(total_cost, 2)
            }

    if not best_option:
        raise ValueError(f"Немає магазину з продуктом '{customer['product']}'")

    return best_option
