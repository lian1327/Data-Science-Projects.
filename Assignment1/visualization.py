import matplotlib.pyplot as plt

# Data for the bookstore inventory
genres = ["Mystery", "Western", "Non Fiction", "Fiction", "Teen Fiction", "Biography", "Science", "Math"]
books_in_stock = [20, 18, 35, 20, 15, 22, 15, 25]

# Creating the dot plot
plt.figure(figsize=(10, 6))
plt.plot(genres, books_in_stock, 'bo')  # 'bo' stands for blue color and circle marker

# Adding title and labels
plt.title("Bookstore Inventory by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Books")

# Displaying the dot plot
plt.show()
