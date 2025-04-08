from file_manager import read, write

def user_menu():
    print("""
User menu:
    1. Show all products
    2. Order
    3. My orders
    4. Logout
    """)

    phone = input("Enter your phone number to track your orders: ")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            print("All products:")
            products = read("products.csv")
            for product in products:
                print(product)

        elif choice == "2":
            product_id = input("Enter product ID to order: ")
            write("new_orders.csv", [phone, product_id], mode="a")
            print("Order placed.")

        elif choice == "3":
            orders = read("new_orders.csv") + read("accepted_orders.csv") + read("canceled_orders.csv")
            print("Your orders:")
            for order in orders:
                if order[0] == phone:
                    print(order)

        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice")
