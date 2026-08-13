print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++Supermarket ++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
def display():
    print("====================================")
    for product_id, details in product.items():
        print(f"|Product ID: {product_id}")
        for key, value in details.items():
            print(f"|{key}:{value}")
    print("====================================")
#==========================
def search(product_name=None):
    for values in product.values():
        if values.get(product_name)!=None:
            return True
        else:
            return False
#==============================
def add():
    product_name=input("enter the product's name:")
    product_category=input("Enter the category:")
    product_price=float(input("Enter the price:"))
    product_stocks=int(input("Enter the Stocks:"))
    if search(product_name):
        print("Product Exists")
    else:
        product_id=f"PRODUCT{len(product)+1:04}"
        product[product_id]={
            "name":product_name,
            "category":product_category,
            "price":product_price,
            "stocks":product_stocks
            }
        print("Product Succesfully Added")
#================================
def update():
    print("Updating")
def delete():
    print("Deleting")
product=dict()
def main():
    while True:
        print("\n1. Display")
        print("2. Search")
        print("3. Add")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                display()
            case 2:
                search()
            case 3:
                add()
            case 4:
                update()
            case 5:
                delete()
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid Choice")
if __name__=="__main__":
    main()
