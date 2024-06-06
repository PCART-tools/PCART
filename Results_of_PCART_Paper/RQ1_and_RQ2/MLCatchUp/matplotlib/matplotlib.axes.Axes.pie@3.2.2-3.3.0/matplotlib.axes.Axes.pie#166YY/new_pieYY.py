import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, True, labeldistance=1.05, counterclock=False, wedgeprops={'edgecolor': 'black'}, startangle=90, radius=False, data=None, normalize=None)
