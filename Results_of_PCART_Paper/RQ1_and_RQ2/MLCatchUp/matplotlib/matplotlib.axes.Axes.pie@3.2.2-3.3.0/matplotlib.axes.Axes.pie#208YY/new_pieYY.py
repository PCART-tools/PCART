import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(explode=explode, startangle=90, counterclock=False, labels=labels, radius=False, data=None, labeldistance=1.05, shadow=True, textprops={'color': 'white'}, wedgeprops={'edgecolor': 'black'}, colors=colors, autopct='%1.1f%%', pctdistance=0.85, x=sizes, normalize=None)
