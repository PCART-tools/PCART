import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, pctdistance=0.85, data=None, labels=labels, counterclock=False, startangle=90, shadow=True, wedgeprops={'edgecolor': 'black'}, colors=colors, radius=False, labeldistance=1.05, autopct='%1.1f%%', normalize=None)
