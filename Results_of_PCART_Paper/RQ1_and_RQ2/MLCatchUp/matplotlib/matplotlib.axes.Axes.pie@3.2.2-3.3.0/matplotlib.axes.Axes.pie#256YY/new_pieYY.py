import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, True, labeldistance=1.05, center=(0, 0), radius=False, counterclock=False, startangle=90, textprops={'color': 'white'}, data=None, wedgeprops={'edgecolor': 'black'}, frame=True, normalize=None)
