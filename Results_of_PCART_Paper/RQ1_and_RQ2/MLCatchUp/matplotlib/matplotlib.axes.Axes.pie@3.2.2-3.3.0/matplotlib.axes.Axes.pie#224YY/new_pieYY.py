import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, True, startangle=90, data=None, wedgeprops={'edgecolor': 'black'}, radius=False, center=(0, 0), counterclock=False, textprops={'color': 'white'}, labeldistance=1.05, normalize=None)
