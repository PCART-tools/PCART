import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(data=None, rotatelabels=True, colors=colors, autopct='%1.1f%%', center=(0, 0), startangle=90, wedgeprops={'edgecolor': 'black'}, textprops={'color': 'white'}, counterclock=False, labels=labels, radius=False, pctdistance=0.85, shadow=True, x=sizes, frame=True, explode=explode, labeldistance=1.05, normalize=None)
