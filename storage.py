import json
from enum import Enum
from pathlib import Path
from models import Product, PriceRecord, Category
from datetime import datetime

SAVE_FILE = Path("products.json")

def save_products(products):
    product_data = [{
        'name': product.name,
        'category': product.category.value,
        'current_price': product.current_price,
        'price_history': [{
        'price': record.price,
        'date': record.date.isoformat()
    } for record in product.price_history]
    } for product in products]

    with SAVE_FILE.open("w") as file:
        json.dump(product_data, file, indent=4)

def load_products():
    if not SAVE_FILE.exists():
        return None

    with SAVE_FILE.open("r") as file:
        product_data = json.load(file)

    products = [Product.from_dict(product) for product in product_data]

    return products
