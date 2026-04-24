import json

from rich.prompt import Prompt

sources = ("CARS/car.txt", "BEAUTY/beauty.txt", "FASHION/fashion.txt", "GROCERIES/groceries.txt")
INVENTORY__FILE = "inventory.txt"
PRODUCT_FILE = "product_specification.json"

product_prompt = Prompt.ask('What do you seek? ').upper().strip().rsplit(sep=" ")
product_name = product_prompt[1]

item_found: bool = False
def checkAvailability(item, inventory_dict):
    is_present: bool = False
    if item in inventory_dict:
        is_present = True
        return is_present
    else:
        return f"Error 404: could not be found"


def furtherProductSpecification():
    Prompt.ask("Would you like to see available Options (yes or no)? ")

def locateItem(item, inventory_list=sources):
    completion_message: str = ""
    for i in range(len(inventory_list)):
        try:
            with open(inventory_list[i], "r") as file:
                if item not in file:
                    pass
                else:
                    print("The Item has been found")
                    completion_message = f"The {item} was found in {inventory_list[i]}"
                    break

        except FileNotFoundError:
            print("File does not Exist")
        except PermissionError:
            print("You do not have permission to read this file")

#    try:
#         with open("product_specification.json", "r") as file:
#             json.load(file)
#             if item not in file:
#                 pass
#             else:
#                 completion_message = f"The {item} was found in {file}"
#
#     except FileNotFoundError:
#         print("File does not Exist")
#     except PermissionError:
#         print("You do not have permission to read this file")
#     return completion_message

def fetchInventory():
    with open(INVENTORY__FILE, "r") as file:
        available_items = {}
        for item in file:
            indexed_item, available_units = item.strip().split(",")
            available_items[indexed_item] = available_units
    return available_items


print(locateItem(product_name))