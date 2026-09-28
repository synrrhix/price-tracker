from collections import Counter, defaultdict
from datetime import datetime
from typing import Optional

from models import Product, PriceRecord, Category


def find_product(products, name) -> Optional[Product]:
    name = name.strip().lower()

    for product in products:
        if product.name.lower() == name:
            return product

    return None


def get_valid_price(prompt):
    """Keep asking until the user enters a valid non-negative price."""
    while True:
        price_input = input(prompt).strip()

        try:
            price = float(price_input)

            if price < 0:
                print("Price cannot be negative. Try again.")
                continue

            return price

        except ValueError:
            print(f"'{price_input}' is not a valid number. Try again.")


def get_valid_category(prompt):
    """Keep asking until the user enters a valid Category."""
    while True:
        category_name = input(prompt).strip().title()

        try:
            return Category(category_name)

        except ValueError:
            print(f"'{category_name}' is not a valid category.")
            print("Available categories:")

            for category in Category:
                print(f"- {category.value}")


def add_product(products):
    name = input("Enter product name: ").strip().title()

    if not name:
        print("Product name cannot be empty.")
        return None

    if find_product(products, name) is not None:
        print(f"A product called '{name}' already exists.")
        return None

    category = get_valid_category("Enter category: ")
    new_price = get_valid_price(f"Enter new price for {name}: ")

    product = Product(name, category, new_price)
    products.append(product)

    return product


def add_price(product):
    new_price = get_valid_price(
        f"Enter new price for {product.name}: "
    )

    while True:
        date_input = input(
            "Enter date (e.g. YYYY-MM-DD): "
        ).strip()

        try:
            parsed_date = datetime.strptime(
                date_input,
                "%Y-%m-%d"
            )
            break

        except ValueError:
            print(
                f"'{date_input}' is not a valid date "
                "in YYYY-MM-DD format. Try again."
            )

    record = PriceRecord(
        new_price,
        parsed_date.date()
    )

    product.price_history.append(record)
    product.current_price = new_price

    return product


def update_product(products, name):
    product = find_product(products, name)

    if product is None:
        print("Product not found.")
        return None

    new_name = input(
        f"Enter new name "
        f"(leave blank to keep '{product.name}'): "
    ).strip()

    if new_name:
        new_name = new_name.title()
        existing_product = find_product(products, new_name)

        if existing_product is not None and existing_product is not product:
            print(
                f"A product called '{new_name}' already exists. "
                "Name not changed."
            )
        else:
            product.name = new_name

    category_input = input(
        f"Enter new category "
        f"(leave blank to keep '{product.category.value}'): "
    ).strip()

    if category_input:
        try:
            product.category = Category(category_input.title())

        except ValueError:
            print("Invalid category. Category not changed.")

    return product


def remove_product(products, name):
    product = find_product(products, name)

    if product is None:
        print("Product not found.")
        return

    products.remove(product)
    print(f"'{product.name}' removed successfully.")


def show_products(products):
    if not products:
        print("No products.")
        return

    print("===== YOUR PRODUCTS =====")

    for product in products:
        product_details = [
            product.name,
            product.category.value,
            f"£{product.current_price:.2f}"
        ]

        joined_products = " | ".join(product_details)
        print(joined_products)


def average_prices(*prices):
    if not prices:
        return None

    return sum(prices) / len(prices)


def create_product(**details):
    """
    Create a Product using keyword arguments.

    Example:
    create_product(
        name="Airpods",
        category=Category.AUDIO,
        price=149.99
    )
    """
    details["current_price"] = details.pop("price")
    return Product(**details)


def count_categories(products):
    categories = [
        product.category.value
        for product in products
    ]

    return Counter(categories)


def most_common_category(products):
    counts = count_categories(products)

    if not counts:
        return None

    return counts.most_common(1)[0]


def group_by_category(products):
    grouped = defaultdict(list)

    for product in products:
        grouped[product.category.value].append(product.name)

    return grouped

def price_drops(product):
    for i in range(1, len(product.price_history)):
        previous = product.price_history[i - 1].price
        new = product.price_history[i].price

        if new < previous:
            yield previous, new

def total_price_drops(product):
    total = 0

    for previous, new in price_drops(product):
        total += previous - new

    return total


def print_price_drops(product):
    found_drop = False

    for previous, new in price_drops(product):
        found_drop = True

        difference = previous - new

        print(
            f"£{previous:.2f} → "
            f"£{new:.2f}  "
            f"(-£{difference:.2f})"
        )

    if not found_drop:
        print("No price drops recorded.")