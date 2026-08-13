print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++ Supermarket +++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
product = dict()
# ==========================
def display():
    if not product:
        print("No products available.")
        return
    print("====================================")
    for product_id, details in product.items():
        print(f"| Product ID: {product_id}")
        for key, value in details.items():
            print(f"| {key.capitalize()}: {value}")
        print("====================================")
# ==========================
def search(product_name=None):
    if product_name is None:
        product_name = input("Enter the product name to search: ").strip()
    for p_id, details in product.items():
        if details.get("name", "").lower() == product_name.lower():
            return p_id
    return None
# ==========================
def add():
    try:
        product_name = input("Enter the product's name: ").strip()
        if not product_name:
            print("Product name cannot be empty.")
            return
        if search(product_name):
            print("Product already exists!")
            return
        product_category = input("Enter the category: ").strip()
        product_price = float(input("Enter the price: "))
        product_stocks = int(input("Enter the stocks: "))
        product_id = f"PRODUCT{len(product) + 1:04d}"
        product[product_id] = {
            "name": product_name,
            "category": product_category,
            "price": product_price,
            "stocks": product_stocks
        }
        print("Product Successfully Added!")
    except ValueError:
        print("Invalid input! Price must be a number and stocks must be an integer.")
    except Exception as e:
        print(f"Can't add product: {e}")
# ==========================
def update():
    product_name = input("Enter the product name to update: ").strip()
    product_id = search(product_name)
    if not product_id:
        print("Product doesn't exist.")
        return
    print(f"\nUpdating Product ID: {product_id}")
    details = product[product_id]
    for key in list(details.keys()):
        choice = input(f"Do you want to update '{key}'? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            try:
                new_val = input(f"Enter new value for {key}: ").strip()
                if key == "price":
                    details[key] = float(new_val)
                elif key == "stocks":
                    details[key] = int(new_val)
                else:
                    details[key] = new_val
                print(f"'{key}' updated successfully.")
            except ValueError:
                print(f"Invalid input type for {key}. Update skipped.")
# ==========================
def delete():
    product_name = input("Enter the product name to delete: ").strip()
    product_id = search(product_name)
    if product_id:
        del product[product_id]
        print(f"Product '{product_name}' successfully deleted.")
    else:
        print("Product doesn't exist.")
# ==========================
def main():
    while True:
        print("\n1. Display Products")
        print("2. Search Product")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        match choice:
            case "1":
                display()
            case "2":
                p_id = search()
                if p_id:
                    print("\n--- Product Found ---")
                    print(f"ID: {p_id}")
                    for k, v in product[p_id].items():
                        print(f"{k.capitalize()}: {v}")
                else:
                    print("Product not found.")
            case "3":
                add()
            case "4":
                update()
            case "5":
                delete()
            case "6":
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
