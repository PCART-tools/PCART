import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(autopct='%1.1f%%', colors=colors, x=sizes, shadow=True, explode=explode, labels=labels, startangle=90, data=None, pctdistance=0.85, labeldistance=1.05, normalize=None)
