import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(labeldistance=1.05, x=sizes, startangle=90, shadow=True, labels=labels, data=None, radius=False, autopct='%1.1f%%', pctdistance=0.85, counterclock=False, explode=explode, colors=colors, normalize=None)
