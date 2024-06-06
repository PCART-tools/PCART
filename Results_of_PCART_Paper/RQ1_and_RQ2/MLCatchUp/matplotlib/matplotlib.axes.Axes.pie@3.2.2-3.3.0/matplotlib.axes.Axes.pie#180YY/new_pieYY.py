import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(data=None, radius=False, x=sizes, labeldistance=1.05, shadow=True, explode=explode, startangle=90, counterclock=False, pctdistance=0.85, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', colors=colors, labels=labels, normalize=None)
