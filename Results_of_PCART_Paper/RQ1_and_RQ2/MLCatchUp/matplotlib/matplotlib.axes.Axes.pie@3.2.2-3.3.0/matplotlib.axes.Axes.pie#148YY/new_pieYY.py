import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, counterclock=False, data=None, labeldistance=1.05, startangle=90, radius=False, shadow=True, colors=colors, pctdistance=0.85, autopct='%1.1f%%', normalize=None)
