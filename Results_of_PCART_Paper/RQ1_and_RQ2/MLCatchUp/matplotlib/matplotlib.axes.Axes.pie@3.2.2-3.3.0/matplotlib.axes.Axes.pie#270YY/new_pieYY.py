import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(labels=labels, colors=colors, labeldistance=1.05, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, data=None, radius=False, frame=True, counterclock=False, textprops={'color': 'white'}, center=(0, 0), explode=explode, startangle=90, autopct='%1.1f%%', x=sizes, shadow=True, normalize=None)
