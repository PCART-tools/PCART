import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, textprops={'color': 'white'}, radius=False, labels=labels, wedgeprops={'edgecolor': 'black'}, explode=explode, autopct='%1.1f%%', center=(0, 0), counterclock=False, shadow=True, startangle=90, rotatelabels=True, data=None, labeldistance=1.05, colors=colors, frame=True, pctdistance=0.85, normalize=None)
