import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, startangle=90, data=None, counterclock=False, colors=colors, labels=labels, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, labeldistance=1.05, pctdistance=0.85, radius=False, textprops={'color': 'white'}, shadow=True, normalize=None)
