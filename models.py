from datetime import datetime
from enum import Enum


class Category(Enum):
    AUDIO = "Audio"
    GAMING = "Gaming"
    BOOKS = "Books"
    CLOTHING = "Clothing"
    ELECTRONICS = "Electronics"
    HOME = "Home"
    KITCHEN = "Kitchen"
    FURNITURE = "Furniture"
    TOYS = "Toys"
    SPORTS = "Sports"
    BEAUTY = "Beauty"
    GROCERIES = "Groceries"
    OFFICE = "Office"
    GARDEN = "Garden"
    PETS = "Pets"
    AUTOMOTIVE = "Automotive"
    HEALTH = "Health"
    JEWELLERY = "Jewellery"
    MUSIC = "Music"
    FOOTWEAR = "Footwear"


class PriceRecord:
    def __init__(self, price, date):
        self.price = price
        self.date = date

    def __str__(self):
        return f'£{self.price:.2f} - {self.date}'


class Product:
    def __init__(self, name, category, current_price, price_history=None):
        self.name = name
        self.category = category
        self.current_price = current_price

        if price_history is not None:
            self.price_history = price_history
        else:
            self.price_history = [
                PriceRecord(current_price, datetime.now().date())
            ]

    def __str__(self):
        return (
            f'{self.name} | '
            f'{self.category.value} | '
            f'£{self.current_price:.2f}'
        )

    def show_price_history(self):
        print(f'===== {self.name.upper()} PRICE HISTORY =====')

        if not self.price_history:
            print('No price history.')
            return

        for record in self.price_history:
            print(record)

    @property
    def lowest_price(self):
        if not self.price_history:
            return None

        return min(record.price for record in self.price_history)

    @property
    def highest_price(self):
        if not self.price_history:
            return None

        return max(record.price for record in self.price_history)

    @property
    def percentage_change(self):
        if not self.price_history:
            return None

        first_price = self.price_history[0].price

        if first_price == 0:
            return None

        return (
            (self.current_price - first_price)
            / first_price
            * 100
        )
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            category=Category(data['category']),
            current_price=data['current_price'],
            price_history = [
                PriceRecord(
                    record["price"],
                    datetime.strptime(record["date"], "%Y-%m-%d").date()
                )
                for record in data.get("price_history",[])
        ]
        )

    @staticmethod
    def validate_price(price):
        return price >= 0