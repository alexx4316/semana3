inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

def menu():
    print("welcome to elmascapito bookstore\n 1. Add book\n 2. Search book\n" 
    " 3. Update price\n 4. Delete book\n 5. Total inventory price")

def new_books(title,price,quantity):
    inventorys = {
         "title":title,
         "price":price,
         "quantity":quantity
    }
    inventory.append(inventorys)

def search_books(title):
    for inventorys in inventory:
        if inventorys["title"] == title:
            print(f"Title: {inventorys['title']}, Price: {inventorys['price']}, Quantity: {inventorys['quantity']} ")
            return inventorys
    else:
        print(f"the book entered is not in the list")

def update_price(title,new_price):
    for inventorys in inventory:
        if inventorys["title"] == title:
            inventorys["price"] = new_price
        print(f"the price of the book: {title} has been update")
    print(f"the book: {title} is not in the inventary")

def delete_book(title):
    for inventorys in inventory:
        if inventorys["title"] == title:
            inventory.remove(inventorys)
            print(f"the book: {title} has been eliminate")
            return True
    print(f"the book: {title} is not in the inventary")
    return False

def calculate_total():
    total = 0
    for inventorys in inventory:
        total += inventorys["price"] * inventorys["quantity"]
    return total

while True:
    menu()
    option_str = input("Enter the desired option: ").strip()
    option = int(option_str)
    if not option_str.isdigit():
        print("Invalid option")
        continue

    match option:
        case 1:
            try:
                title = str(input("Enter the title of the book: ")).strip().lower()
                if not title:
                    raise ValueError("The name cannot be empty")
                price = float(input("Enter the price of the book: "))
                if price < 0:
                    raise ValueError("The price cannot be negative")
                quantity = int(input("Enter the quantity of books: "))
                if quantity < 0:
                    raise ValueError("The quantity cannot be negative")
                new_books(title, price, quantity)
            except ValueError as e:
                print(f"Error: {e}. Try again")
        case 2:
            try:
                title = input("Enter the name of the book you are interested in: ").strip().lower()
                if not title:  
                    raise ValueError("The name cannot be empty")
                search_books(title)
            except ValueError as e:
                print(f"Error {e}. Try again")
        case 3:            
            try:
                title = str(input("Enter the title of the book: "))
                if not title:
                    raise ValueError("The name cannot be empty")
                new_price = float(input("Enter the new book value: "))
                if new_price < 0:
                    raise ValueError("The price cannot be negative")
                update_price(title, new_price)
            except ValueError as e:
                print(f"Error {e}. Try again")
        case 4:
            try:
                title = str(input("Enter the title of the book you want to delete: "))
                if not title:
                    raise ValueError("The name cannot be empty")
                delete_book(title)
            except ValueError as e:
                print(f"Error {e}. Try again")
        case 5:
            print(f"The total inventory is: {calculate_total():.2f}")
        case 6:
            print("Exit program")
            break
        case _:
            print("Invalid option, choose an option from the menu.")
