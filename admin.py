from file_manager import read, write

def admin_menu():
    print("""
Admin menu:
    1. New orders
    2. Accepted orders
    3. Canceled orders
    4. Add new product
    5. Delete product
    6. Logout
    """)

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("New orders:")
            orders = read("new_orders.csv")
            for order in orders:
                print(order)

        elif choice == "2":
            print("Accepted orders:")
            orders = read("accepted_orders.csv")
            for order in orders:
                print(order)

        elif choice == "3":
            print("Canceled orders:")
            orders = read("canceled_orders.csv")
            for order in orders:
                print(order)

        elif choice == "4":
            name = input("Product name: ")
            price = input("Price: ")
            products = read("products.csv")
            new_id = str(int(products[-1][0]) + 1) if products else "1"
            write("products.csv", [new_id, name, price], mode="a")
            print("Product added.")

        elif choice == "5":
            products = read("products.csv")
            for p in products:
                print(p)
            del_id = input("Enter product ID to delete: ")
            updated = [p for p in products if p[0] != del_id]
            write("products.csv", updated)
            print("Product deleted.")

        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice")
