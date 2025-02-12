# Creating a dictionary of shoe brands and their popular models
shoe_brands = {
    "Nike": "Air Max",
    "Adidas": "Stan Smith",
    "Puma": "Suede",
    "Reebok": "Classic"
}

print("Original shoe_brands dictionary:", shoe_brands)

# Using the get() method
nike_model = shoe_brands.get("Nike")
print(f"Nike's popular model: {nike_model}")

new_balance_model = shoe_brands.get("New Balance")
print(f"New Balance's popular model: {new_balance_model}")

new_balance_model_default = shoe_brands.get("New Balance", "550")
print(f"New Balance's popular model (with default): {new_balance_model_default}")


# Changing a value
shoe_brands["Adidas"] = "Superstar"
print("shoe_brands after changing Adidas:", shoe_brands)

# Adding an item
shoe_brands["Under Armour"] = "HOVR"
print("shoe_brands after adding Under Armour:", shoe_brands)

# Creating a nested dictionary
shoe_details = {
    "Nike": {"model": "Air Max", "category": "Running"},
    "Adidas": {"model": "Superstar", "category": "Lifestyle"},
    "Puma": {"model": "Suede", "category": "Lifestyle"},
    "Reebok": {"model": "Classic", "category": "Lifestyle"},
    "Under Armour": {"model": "HOVR", "category": "Running"}
}

print("shoe_details nested dictionary:", shoe_details)

nike_category = shoe_details["Nike"]["category"]
print(f"Nike's category: {nike_category}")

# Using the fromkeys() method
shoe_brands_list = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour", "New Balance"]
default_value = "Unknown"

new_shoe_dict = dict.fromkeys(shoe_brands_list, default_value)
print("new_shoe_dict created with fromkeys:", new_shoe_dict)

new_shoe_dict["Nike"] = "Air Force 1"
print("new_shoe_dict after updating Nike:", new_shoe_dict)