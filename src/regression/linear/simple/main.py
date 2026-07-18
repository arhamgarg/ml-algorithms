import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

mean_x = np.mean(x)
mean_y = np.mean(y)

m = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
c = mean_y - m * mean_x

print(f"Model: y = {c} + {m}*x")

plt.scatter(x, y, color="red", marker="o", s=30)
y_pred = c + m * x
plt.plot(x, y_pred, color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simple Linear Regression")
plt.show()
