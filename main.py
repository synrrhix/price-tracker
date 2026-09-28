from models import Product
from tracker import find_product, add_product, remove_product, show_products, add_price, update_product, group_by_category
from storage import save_products, load_products

def main():
    products = []

    while True:
        print("\n===== PRICE TRACKER =====")
        print("1. Show products")
        print("2. Add product")
        print("3. Remove product")
        print("4. Find product")
        print("5. Update price")
        print("6. Update product details")
        print("7. View price history")
        print("8. Product statistics")
        print("9. Save products")
        print("10. Load products")
        print("11. Group by category")
        print("12. Exit")

        choice = input("> ").strip()

        if choice == "1":
            show_products(products)

        elif choice == "2":
            product = add_product(products)
            print(f"{product.name} added successfully.")

        elif choice == "3":
            name = input("Enter product name to remove: ").strip().title()
            remove_product(products, name)

        elif choice == "4":
            name = input("Enter product name to find: ").strip().title()
            product = find_product(products, name)

            if product is None:
                print("Product not found.")
            else:
                print(product)

        elif choice == "5":
            name = input("Enter product name: ").strip().title()
            product = find_product(products, name)

            if product is None:
                print("Product not found.")
            else:
                add_price(product)
                print(f"Updated price: ${product.current_price:.2f}")

        elif choice == "6":
            name = input("Enter product name to update: ").strip().title()
            update_product(products, name)

        elif choice == "7":
            name = input("Enter product name: ").strip().title()
            product = find_product(products, name)

            if product is None:
                print("Product not found.")
            else:
                product.show_price_history()

        elif choice == "8":
            name = input("Enter product name: ").strip().title()
            product = find_product(products, name)

            if product is None:
                print("Product not found.")
            else:
                print("\n===== PRODUCT STATISTICS =====")
                print(f"Product:               {product.name}")
                print(f"Category:              {product.category}")
                print(f"Current price:         ${product.current_price:.2f}")

                if product.lowest_price is None:
                    print("Lowest price:          No price history")
                else:
                    print(f"Lowest price:          ${product.lowest_price:.2f}")

                if product.highest_price is None:
                    print("Highest price:         No price history")
                else:
                    print(f"Highest price:         ${product.highest_price:.2f}")

                if product.percentage_change is None:
                    print("Percentage change:     No price history")
                else:
                    print(f"Percentage change:     {product.percentage_change:.2f}%")

                print(f"Price records:         {len(product.price_history)}")

        elif choice == "9":
            save_products(products)
            print("Products saved successfully.")

        elif choice == "10":
            loaded_products = load_products()

            if loaded_products is None:
                print("No save file found.")
            else:
                products = loaded_products
                print("Products loaded successfully.")

        elif choice == "11":
            grouped = group_by_category(products)

            for category, product_names in grouped.items():
                print(f"\n{category}:")

                for product_name in product_names:
                    print(f"  - {product_name}")

        elif choice == "12":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()