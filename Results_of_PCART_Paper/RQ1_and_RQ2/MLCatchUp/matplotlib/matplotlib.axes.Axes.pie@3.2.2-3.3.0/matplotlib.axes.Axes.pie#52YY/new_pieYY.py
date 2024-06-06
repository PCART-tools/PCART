import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, pctdistance=0.85, data=None, labels=labels, autopct='%1.1f%%', explode=explode, colors=colors, normalize=None)
