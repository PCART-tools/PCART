import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, pctdistance=0.85, wedgeprops={'edgecolor': 'black'}, labeldistance=1.05, center=(0, 0), shadow=True, data=None, startangle=90, textprops={'color': 'white'}, frame=True, radius=False, counterclock=False, autopct='%1.1f%%', normalize=None)
