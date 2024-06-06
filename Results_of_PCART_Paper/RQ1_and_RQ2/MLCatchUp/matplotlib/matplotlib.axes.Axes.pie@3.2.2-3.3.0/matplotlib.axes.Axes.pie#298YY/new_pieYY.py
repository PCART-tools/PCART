import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, radius=False, frame=True, shadow=True, autopct='%1.1f%%', data=None, pctdistance=0.85, counterclock=False, textprops={'color': 'white'}, center=(0, 0), labeldistance=1.05, startangle=90, wedgeprops={'edgecolor': 'black'}, colors=colors, rotatelabels=True, normalize=None)
