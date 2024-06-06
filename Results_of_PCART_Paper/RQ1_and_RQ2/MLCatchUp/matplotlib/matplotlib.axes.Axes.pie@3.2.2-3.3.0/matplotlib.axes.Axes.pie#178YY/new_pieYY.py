import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, labels=labels, shadow=True, data=None, counterclock=False, startangle=90, labeldistance=1.05, colors=colors, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, autopct='%1.1f%%', radius=False, explode=explode, normalize=None)
