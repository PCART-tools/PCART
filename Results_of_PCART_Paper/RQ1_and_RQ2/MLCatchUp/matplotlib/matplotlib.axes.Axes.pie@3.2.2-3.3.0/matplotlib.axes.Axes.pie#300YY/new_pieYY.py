import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, startangle=90, center=(0, 0), data=None, colors=colors, frame=True, labels=labels, autopct='%1.1f%%', pctdistance=0.85, counterclock=False, shadow=True, textprops={'color': 'white'}, rotatelabels=True, labeldistance=1.05, wedgeprops={'edgecolor': 'black'}, radius=False, normalize=None)
