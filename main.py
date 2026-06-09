
fuel_inventory = 1000

regular_price = 3
premium_price = 4

total_sales = 0

while True:
    print("\nGAS STATION")
    print("1 - Buy Regular Gas ($3 per gallon)")
    print("2 - Buy Premium Gas ($4 per gallon)")
    print("3 - View Fuel Inventory")
    print("4 - Exit")

    choice = input("Select Option: ")

    if choice == "1":
        gallons = float(input("Enter gallons: "))

        if gallons <= fuel_inventory:
            cost = gallons * regular_price
            fuel_inventory = fuel_inventory - gallons
            total_sales = total_sales + cost

            print("Fuel Dispensed!")
            print("Cost: $", cost)
        else:
            print("Not enough fuel available!")

    elif choice == "2":
        gallons = float(input("Enter gallons: "))

        if gallons <= fuel_inventory:
            cost = gallons * premium_price
            fuel_inventory = fuel_inventory - gallons
            total_sales = total_sales + cost

            print("Fuel Dispensed!")
            print("Cost: $", cost)
        else:
            print("Not enough fuel available!")

    elif choice == "3":
        print("Fuel Remaining:", fuel_inventory, "gallons")
        print("Total Sales: $", total_sales)

    elif choice == "4":
        print("Gas Station Closed")
        break

    else:
        print("Invalid Option!")
