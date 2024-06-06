import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors=colors, labeldistance=1.05, radius=False, textprops={'color': 'white'}, shadow=True, wedgeprops={'edgecolor': 'black'}, pctdistance=0.85, data=None, counterclock=False, startangle=90, autopct='%1.1f%%', normalize=None)
