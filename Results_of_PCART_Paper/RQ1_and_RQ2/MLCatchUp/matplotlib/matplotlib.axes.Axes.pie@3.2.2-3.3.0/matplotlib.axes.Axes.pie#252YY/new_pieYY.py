import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, True, 1.05, 90, counterclock=False, data=None, center=(0, 0), wedgeprops={'edgecolor': 'black'}, frame=True, textprops={'color': 'white'}, radius=False, normalize=None)
