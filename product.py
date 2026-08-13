print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++Supermarket ++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
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
                print("User Wants to Display the Product")
            case 2:
                print("User Wants to Search the Product")
            case 3:
                print("User Wants to Add a Product")
            case 4:
                print("User Wants to Update")
            case 5:
                print("User Wants to Delete")
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid Choice")
if __name__=="__main":
    main()
