import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, colors=colors, frame=True, labeldistance=1.05, data=None, startangle=90, pctdistance=0.85, center=(0, 0), radius=False, counterclock=False, explode=explode, labels=labels, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, shadow=True, textprops={'color': 'white'}, normalize=None)
