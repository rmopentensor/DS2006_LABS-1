# Keep track of inventory:
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "grape": 40,
    "pear": 25

}

def display_inventory():
    print("\nCurrent inventory stock:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print()

def add_item(item, amount):
    if item in inventory:
        inventory[item] += amount
    else:
        inventory[item] = amount
    print(f"Added {amount} {item}(s).")

def remove_item(item, amount):
    if item in inventory:
        if amount <= inventory[item]:
            inventory[item] -= amount
            print(f"Removed {amount} {item}(s).")
            if inventory[item] == 0:
                print(f"{item} is now out of stock.")
        else:
            print(f"Cannot remove {amount} {item}(s); only {inventory[item]} available.")
    else:
        print(f"{item} not found in inventory.")

def check_quantity(item):
    if item in inventory:
        print(f"Quantity of {item}: {inventory[item]}")
    else:
        print(f"{item} not found in inventory.")

def main():
    while True:
        print("Choose an option: add, remove, check, show")
        choice = input("Option: ").lower()

        if choice == "add":
            item = input("Enter item to add: ").lower()
            amount = int(input(f"How many {item}s to add? "))
            add_item(item, amount)

        elif choice == "remove":
            item = input("Enter item to remove: ").lower()
            amount = int(input(f"How many {item}s to remove? "))
            remove_item(item, amount)

        elif choice == "check":
            item = input("Enter item to check quantity: ").lower()
            check_quantity(item)

        elif choice == "show":
            display_inventory()

        else:
            print("Invalid option. Please choose add, remove, check, or show.")

if __name__ == "__main__":
    main()
