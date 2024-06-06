import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', pctdistance=0.85, center=(0, 0), labeldistance=1.05, textprops={'color': 'white'}, shadow=True, counterclock=False, data=None, startangle=90, radius=False, wedgeprops={'edgecolor': 'black'}, normalize=None)
