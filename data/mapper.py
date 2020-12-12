import matplotlib.pyplot as plt

hfont = {"fontname" : "Helvetica Neue"}

years = [1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

number = [54, 63, 99, 111, 189, 208, 232, 233, 272]


plt.title("Women's Participation, Winter Olympics Between 1984 -2014", pad="20", **hfont)

plt.plot(years, number, color=(0/255,100/255,100/255), linewidth=3.0)
plt.ylabel ("Number of Women Participants")
plt.xlabel ("Olympic Year")
plt.show()