import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', startangle=90, pctdistance=0.85, labeldistance=1.05, center=(0, 0), shadow=True, counterclock=False, frame=True, rotatelabels=True, textprops={'color': 'white'}, radius=False, data=None, wedgeprops={'edgecolor': 'black'}, normalize=None)
