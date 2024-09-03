# shoe.py


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# =============Shoe list===========
shoe_list = []


def read_shoes_data():
    """Read shoes data from the inventory file and populate the shoe_list."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                if line.strip():  # Skip empty lines
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("The file inventory.txt does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    """Capture shoe data from user input and add it to the shoe_list."""
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")

        # Validate cost input
        cost = float(input("Enter the cost: "))
        if cost < 0:
            raise ValueError("Cost cannot be negative.")

        # Validate quantity input
        quantity = int(input("Enter the quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        append_to_inventory_file(shoe)  # Append the new shoe to the file
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_all():
    """Print all shoes in the shoe_list."""
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """Find the shoe with the lowest quantity and update its stock."""
    if not shoe_list:
        print("No shoes in the inventory.")
        return

    shoe_to_restock = min(shoe_list, key=lambda s: s.get_quantity())
    print(f"The shoe with the lowest quantity is: {shoe_to_restock}")

    try:
        additional_quantity = int(input("Enter the quantity to add: "))
        if additional_quantity < 0:
            raise ValueError("Quantity to add cannot be negative.")
        shoe_to_restock.quantity += additional_quantity
        update_inventory_file()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def search_shoe():
    """Search for a shoe by its code."""
    code = input("Enter the shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")


def value_per_item():
    """Calculate and print the value of each shoe based on its cost and quantity."""
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Code: {shoe.code}, Product: {shoe.product}, Total Value: {value}")


def highest_qty():
    """Find and print the shoe with the highest quantity."""
    if not shoe_list:
        print("No shoes in the inventory.")
        return

    shoe_with_highest_qty = max(shoe_list, key=lambda s: s.get_quantity())
    print(
        f"The product with the highest quantity is: {shoe_with_highest_qty.product}, Quantity: {shoe_with_highest_qty.quantity}"
    )


def append_to_inventory_file(shoe):
    """Append a single shoe entry to the inventory file."""
    try:
        with open("inventory.txt", "a") as file:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")


def update_inventory_file():
    """Update the inventory file with the current shoe_list."""
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")


# ==========Main Menu=============
def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nShoe Inventory Management System")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-stock Shoes")
        print("5. Search Shoe")
        print("6. Calculate Value per Item")
        print("7. Shoe with Highest Quantity")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
