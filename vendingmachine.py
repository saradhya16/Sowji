def display_items(items):
    print("Items available:")
    for code, details in items.items():
        print(f"{code}: {details['name']} - ${details['price']:.2f}")

def vending_machine():
    # Define items available in the vending machine
    items = {
        'A1': {'name': 'Soda', 'price': 1.50},
        'A2': {'name': 'Chips', 'price': 1.00},
        'A3': {'name': 'Candy', 'price': 0.75},
        'A4': {'name': 'Juice', 'price': 2.00},
        'A5': {'name': 'Water', 'price': 1.25}
    }

    # Display available items
    display_items(items)

    # Ask the user to select an item
    choice = input("Please select an item by entering the code (e.g., A1): ").upper()

    # Check if the selected item is available
    if choice in items:
        selected_item = items[choice]
        print(f"You selected {selected_item['name']} which costs ${selected_item['price']:.2f}")
        
        # Ask the user to insert money
        money_inserted = float(input("Please insert money: $"))
        
        # Check if enough money was inserted
        if money_inserted >= selected_item['price']:
            change = money_inserted - selected_item['price']
            print(f"Dispensing {selected_item['name']}...")
            if change > 0:
                print(f"Returning change: ${change:.2f}")
            print("Thank you for your purchase!")
        else:
            print(f"Insufficient funds. {selected_item['name']} costs ${selected_item['price']:.2f} but you inserted ${money_inserted:.2f}.")
            print("Please insert the correct amount.")
    else:
        print("Invalid selection. Please try again.")

# Run the vending machine simulation
vending_machine()
