orders = []   

TAX_RATE = 0.18


def book_repair():
    print("\n--- Book New Repair Order ---")

    customer_name = input("Enter customer name: ")
    device_type = input("Enter device type: ")
    issue = input("Enter issue description: ")
    due_date = input("Enter due date (DD/MM/YYYY): ")

    order = {
        "customer": customer_name,
        "device": device_type,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending"
    }

    orders.append(order)
    print("\nRepair order booked successfully!")


def generate_bill():
    if len(orders) == 0:
        print("\nNo repair orders available.")
        return

    print("\n--- Generate Bill ---")
    customer_name = input("Enter customer name: ")

    for order in orders:
        if order["customer"] == customer_name:
            print("\nRepair Order Found")

            repair_fee = float(input("Enter repair fee: ₹"))
            parts_cost = float(input("Enter parts replacement cost: ₹"))

            subtotal = repair_fee + parts_cost
            tax = subtotal * TAX_RATE
            discount = float(input("Enter discount amount (₹): "))

            total = subtotal + tax - discount

            print("\n--------- INVOICE ---------")
            print("Customer Name :", order["customer"])
            print("Device Type   :", order["device"])
            print("Issue         :", order["issue"])
            print("Repair Fee    : ₹", repair_fee)
            print("Parts Cost    : ₹", parts_cost)
            print("Tax (18%)     : ₹", tax)
            print("Discount      : ₹", discount)
            print("---------------------------")
            print("Total Amount  : ₹", total)
            print("---------------------------")

            order["status"] = "Completed"
            return

    print("\nCustomer not found!")


def view_orders():
    if len(orders) == 0:
        print("\nNo orders to display.")
        return

    print("\n--- Repair Orders ---")
    for i, order in enumerate(orders, start=1):
        print(f"\nOrder {i}")
        print("Customer:", order["customer"])
        print("Device  :", order["device"])
        print("Issue   :", order["issue"])
        print("Due Date:", order["due_date"])
        print("Status  :", order["status"])


def main_menu():
    while True:
        print("\n====== FixTrack Menu ======")
        print("1. Book Repair Order")
        print("2. Generate Bill")
        print("3. View Repair Orders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            book_repair()
        elif choice == "2":
            generate_bill()
        elif choice == "3":
            view_orders()
        elif choice == "4":
            print("\nThank you for using FixTrack!")
            break
        else:
            print("\nInvalid choice. Try again.")


# Program execution starts here
main_menu()
