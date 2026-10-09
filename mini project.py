
cars = [
    {"id": 1, "name": "Swift", "price": 1500, "available": True},
    {"id": 2, "name": "Creta", "price": 2500, "available": True},
    {"id": 3, "name": "Nexon", "price": 2000, "available": True},
    {"id": 4, "name": "Honda City", "price": 2200, "available": True}
]


def show_cars():
    print("\nAvailable Cars")

    for car in cars:
        if car["available"]:
            print(car["id"], car["name"], "Rs.", car["price"], "per day")


def rent_car():
    show_cars()

    try:
        car_id = int(input("Enter car ID: "))

        for car in cars:
            if car["id"] == car_id:
                if car["available"]:
                    name = input("Enter your name: ")
                    days = int(input("Enter rental days: "))

                    if name.strip() != "" and days > 0:
                        total = car["price"] * days
                        car["available"] = False

                        with open("records.txt", "a") as file:
                            file.write(
                                name + " rented " + car["name"]
                                + " for " + str(days)
                                + " days. Total = Rs. "
                                + str(total) + "\n"
                            )

                        print("Car rented successfully!")
                        print("Total rent: Rs.", total)
                    else:
                        print("Enter valid details.")
                else:
                    print("Car is already rented.")
                return

        print("Invalid car ID.")

    except ValueError:
        print("Please enter a valid number.")


def return_car():
    try:
        car_id = int(input("Enter car ID to return: "))

        for car in cars:
            if car["id"] == car_id:
                if not car["available"]:
                    car["available"] = True
                    print("Car returned successfully!")
                else:
                    print("This car is not rented.")
                return

        print("Invalid car ID.")

    except ValueError:
        print("Enter a valid car ID.")


def show_records():
    try:
        with open("records.txt", "r") as file:
            print("\nRental Records")
            print(file.read())
    except FileNotFoundError:
        print("No records found.")


while True:
    print("\n--- CAR RENTAL SYSTEM ---")
    print("1. Show Cars")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Show Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_cars()
    elif choice == "2":
        rent_car()
    elif choice == "3":
        return_car()
    elif choice == "4":
        show_records()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
