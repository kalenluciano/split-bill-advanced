def collect_bill_information():
    number_of_people_splitting = 0
    number_of_items = 0
    subtotal_value = 0
    tax_value = 0
    tip_value = 0

    # Get number of people to split the bill
    while True:
        try:
            number_of_people_splitting = int(input("Enter number of people to split bill with: "))
            break
        except ValueError:
            print("Invalid input")
            continue

    # Get number of people to split the bill
    while True:
        try:
            number_of_items = int(input("Enter number of items purchased: "))
            break
        except ValueError:
            print("Invalid input")
            continue

    # Get subtotal number
    while True:
        try:
            subtotal_value = float(input("Enter subtotal amount: $"))
            break
        except ValueError:
            print("Invalid input")
            continue

    # Get tax number
    while True:
        try:
            tax_value = float(input("Enter tax amount: $"))
            break
        except ValueError:
            print("Invalid input")
            continue

    # Get tip number
    while True:
        try:
            tip_value = float(input("Enter tip amount: $"))
            break
        except ValueError:
            print("Invalid input")
            continue

    return number_of_people_splitting, number_of_items, subtotal_value, tax_value, tip_value


# Get names and expenses for each person
def expense_collection(number_of_people_splitting, number_of_items):
    item_expense_book = {}
    for number in range(number_of_items):
        key = input("Enter name of item: ")
        value = 0
        while True:
            try:
                value = float(input("Enter how much the item costs: $"))
                break
            except ValueError:
                print("Invalid input")
                continue
        item_expense_book[key] = value

    people_expense_book = {}
    for number in range(number_of_people_splitting):
        key = input("Enter name of person splitting: ")
        # Could possibly flesh value out to take individual purchases and add them up into the dictionary
        value = float(input("Enter how much they spent: $"))
        people_expense_book[key] = value
    return people_expense_book


# Add together tip and tax
def tip_tax_total(tip_value, tax_value):
    tip_tax_total_amount = tip_value + tax_value
    return tip_tax_total_amount


# Split bill
def split_bill(number_of_people_splitting, number_of_items, subtotal_value, tax_value, tip_value):
    people_expense_book = expense_collection(number_of_people_splitting, number_of_items)
    tip_tax_total_amount = tip_tax_total(tip_value, tax_value)
    for key, value in people_expense_book.items():
        percent_of_subtotal = value / subtotal_value
        total_expense = (percent_of_subtotal * tip_tax_total_amount) + value
        people_expense_book[key] = total_expense
    for key, value in people_expense_book.items():
        print(key + " owes $" + str(value))


number_of_people, items, subtotal, tax, tip = collect_bill_information()
split_bill(number_of_people, items, subtotal, tax, tip)
