import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, data=None, autopct='%1.1f%%', counterclock=False, pctdistance=0.85, radius=False, shadow=True, startangle=90, labeldistance=1.05, colors=colors, labels=labels, normalize=None)
