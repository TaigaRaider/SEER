import json
from rich.prompt import Prompt

sources = ("CARS/car.txt", "BEAUTY/beauty.txt", "FASHION/fashion.txt", "GROCERIES/groceries.txt")
INVENTORY__FILE = "inventory.txt"
PRODUCT_FILE = "product_specification.json"

product_prompt = Prompt.ask('What do you seek? ').upper().strip().split(sep=" ")
# product_name = product_prompt[1]

options = []

for i in product_prompt:
    with open(PRODUCT_FILE, "r") as file:
        products: list = json.load(file)

    for item in products:
        if i in item.values():
            options.append(item)

        else:
            products.pop(products.index(item))

print(options)


# def checkAvailability(item, inventory_dict):
#     is_present: bool = False
#     if item in inventory_dict:
#         is_present = True
#         return is_present
#     else:
#         return f"Error 404: could not be found"
#
#
# def furtherProductSpecification():
#     Prompt.ask("Would you like to see available Options (yes or no)? ")
#
#
def locateItem(item, inventory_list=sources):
    itemlocation: str = ""
    item: bool
    for i in range(len(inventory_list)):
        try:
            with open(inventory_list[i], "r") as file:
                if item not in file:
                    itemlocation: bool = False
                else:
                    itemlocation = inventory_list[i]
                    break

        except FileNotFoundError:
            print("File does not Exist")
        except PermissionError:
            print("You do not have permission to read this file")

    return itemlocation
