import matplotlib.pyplot as plt
import numpy as np

# Data
minutes_running = [90, 50, 60, 70, 62, 55, 58, 60]
weight = [180, 178, 179, 177, 180, 179, 177, 176]

# Convert data to NumPy arrays
x = np.array(minutes_running)
y = np.array(weight)

# Calculate necessary sums
N = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Calculate slope (m) and intercept (b)
m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / N

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Generate the regression line
regression_line = m * x + b

# Create the scatter plot
plt.scatter(x, y, color='blue', label='Data Points')

# Plot the regression line
plt.plot(x, regression_line, color='red', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')

# Add labels and legend
plt.xlabel('Minutes Running for the Week')
plt.ylabel('Weight by Week')
plt.title('Scatter Plot with Linear Regression Line')
plt.legend()

# Show the plot
plt.show()