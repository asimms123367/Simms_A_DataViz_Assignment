import matplotlib.pyplot as plt

hfont = {"fontname" : "Helvetica Neue"}

values = [109, 27]
colors = ["black", "green"]
labels = ["CAN", "USA"]

explode = (0, 0.1)

plt.title("Men's Gold Medal Count - USA vs. Canada 2002 -2014", **hfont)
plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()