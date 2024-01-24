from app.data.json_extraction import shops
from app.objects.shop import Shop


shops = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )
    for shop in shops
]
