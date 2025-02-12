
# Create a set.
my_hobbies = {"Reading manga","watching sports","Playing Sports","Taking care of the kids","Cooking"}
my_hobbies2 = {"Reading in General","watching sports","Playing Sports","Taking care of the kids","Cooking"}
# Add an item to a set using the add() method.

diff =  my_hobbies.difference(my_hobbies2)
my_hobbies.add("Cycling")

# Use the remove() method to take an item out of a set.
my_hobbies.remove("Playing Sports")

# Use the difference() method on a set.
print(diff)
