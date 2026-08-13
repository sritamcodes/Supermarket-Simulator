print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++Supermarket ++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
def display():
    print("Displaying")
def search():
    print("Searching")
def add():
    print("Adding")
def update():
    print("Updating")
def delete():
    print("Deleting")
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
