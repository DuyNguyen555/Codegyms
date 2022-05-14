import matplotlib.pyplot as plt
import numpy as np

x = range(50)
y = range(50) + np.random.randint(10,20,50)

sizes = np.random.randint(5, 200, 50)
colors = np.random.randint(0, 100, 50)
plt.scatter(x, y, s=sizes, c=colors, marker='p', alpha=0.5)
plt.show()