from pathlib import Path
import json
filepath = Path("parts.json")


def finditem(itemname):
    match = [item for item in all_items if item["Name"] == itemname]


def load_data():
    if filepath.exists():
        with open(filepath, "r", encoding="UTF-8") as file:
            return json.load(file)
    return {}


def save_data():
    with open(filepath, "w", encoding="UTF-8") as file:
        json.dump(parts, file, indent=4)


parts = load_data()

suspension_list = parts.get("Suspension", [])
engine_list = parts.get("Engine", [])
all_items = suspension_list + engine_list


def update_item(itemname, status):

    for category in parts.values():

        for item in category:

            if item["Name"] == itemname:

                item["Completed"] = status
                save_data()
                return True

    print("Item not found")
    return False


def show_parts():
    for category in parts.values():
        for part in category:
            print(f"Part: {part["Name"]}...Is Completed: {part["Completed"]}")


def show_menu():
    print("1. Show Parts List")
    print("2. Complete an item")
    print("3. Uncomplete an item")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose between 1-4: ")

    if choice == "1":
        show_parts()
    elif choice == "2":
        check = input("Complete Item: ")
        update_item(check, True)
    elif choice == "3":
        uncheck = input("Uncomplete Item: ")
        update_item(uncheck, False)
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")
