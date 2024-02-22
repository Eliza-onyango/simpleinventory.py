# a program to calculate the inventory of an item
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
        print(f"{quantity} {name}(s) added to inventory.")

    def get_item_quantity(self, name):
        if name in self.inventory:
            return self.inventory[name]
        else:
            return 0

    def total_quantity(self):
        return sum(self.inventory.values())


def main():
    inventory = Inventory()

    while True:
        print("\n1. Add item to inventory")
        print("2. Get quantity of an item")
        print("3. Display total quantity of all items")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name: ")
            print(f"Quantity of {name}: {inventory.get_item_quantity(name)}")
        elif choice == '3':
            print(f"Total quantity of all items: {inventory.total_quantity()}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
