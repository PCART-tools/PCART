import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, autopct='%1.1f%%', textprops={'color': 'white'}, startangle=90, pctdistance=0.85, counterclock=False, wedgeprops={'edgecolor': 'black'}, data=None, labeldistance=1.05, radius=False, shadow=True, normalize=None)
