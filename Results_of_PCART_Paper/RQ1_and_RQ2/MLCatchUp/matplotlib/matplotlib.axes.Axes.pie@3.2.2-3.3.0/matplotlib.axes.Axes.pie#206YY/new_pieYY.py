import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, data=None, wedgeprops={'edgecolor': 'black'}, radius=False, labels=labels, labeldistance=1.05, textprops={'color': 'white'}, autopct='%1.1f%%', pctdistance=0.85, explode=explode, startangle=90, shadow=True, colors=colors, counterclock=False, normalize=None)
