import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(labels=labels, textprops={'color': 'white'}, autopct='%1.1f%%', counterclock=False, shadow=True, startangle=90, center=(0, 0), radius=False, colors=colors, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, explode=explode, x=sizes, data=None, labeldistance=1.05, normalize=None)
