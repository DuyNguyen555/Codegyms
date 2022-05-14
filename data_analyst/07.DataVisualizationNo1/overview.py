import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [12.2, 16.3, 20.5, 25.4, 31.2]

plt.plot(x, y, color="r", linewidth=2, linestyle='dashed', marker="o")
plt.title("Matrix ab cv", fontdict={"fontsize": 15, "fontweight": 10, "verticalalignment": "baseline", "horizontalalignment":'left'})
plt.xlabel("X attribute", fontsize=15, color="r", fontweight=1000)
plt.ylabel("Y attribute", fontsize=20, color="g", fontweight=900)
plt.show()