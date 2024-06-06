import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, autopct='%1.1f%%', colors=colors, center=(0, 0), wedgeprops={'edgecolor': 'black'}, labeldistance=1.05, textprops={'color': 'white'}, pctdistance=0.85, startangle=90, radius=False, frame=True, shadow=True, counterclock=False, data=None, normalize=None)
