# Import the datetime module
import datetime

# Get the current date
current_date = datetime.date.today()

# Display the current date
print(f"Today's date: {current_date}")

# You can also format the date in different ways
formatted_date = current_date.strftime("%Y-%m-%d")  # Example: 2023-10-27
print(f"Formatted date: {formatted_date}")

formatted_date_2 = current_date.strftime("%m/%d/%Y")  # Example: 10/27/2023
print(f"Formatted date 2: {formatted_date_2}")

formatted_date_3 = current_date.strftime("%B %d, %Y")  # Example: October 27, 2023
print(f"Formatted date 3: {formatted_date_3}")