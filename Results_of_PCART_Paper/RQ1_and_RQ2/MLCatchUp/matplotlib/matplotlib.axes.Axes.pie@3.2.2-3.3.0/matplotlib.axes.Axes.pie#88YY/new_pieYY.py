import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(colors=colors, x=sizes, data=None, autopct='%1.1f%%', labeldistance=1.05, pctdistance=0.85, explode=explode, labels=labels, shadow=True, normalize=None)
