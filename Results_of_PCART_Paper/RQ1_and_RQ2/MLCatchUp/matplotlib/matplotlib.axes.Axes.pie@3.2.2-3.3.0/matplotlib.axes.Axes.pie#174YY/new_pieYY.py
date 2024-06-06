import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, autopct='%1.1f%%', shadow=True, colors=colors, wedgeprops={'edgecolor': 'black'}, counterclock=False, labeldistance=1.05, startangle=90, data=None, pctdistance=0.85, radius=False, normalize=None)
