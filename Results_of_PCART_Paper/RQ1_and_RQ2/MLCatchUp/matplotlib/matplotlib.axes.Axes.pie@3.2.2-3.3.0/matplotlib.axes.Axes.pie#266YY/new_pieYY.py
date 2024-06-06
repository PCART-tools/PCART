import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, counterclock=False, labels=labels, frame=True, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%', radius=False, startangle=90, labeldistance=1.05, colors=colors, shadow=True, textprops={'color': 'white'}, pctdistance=0.85, center=(0, 0), data=None, normalize=None)
