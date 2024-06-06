import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, pctdistance=0.85, explode=explode, data=None, wedgeprops={'edgecolor': 'black'}, radius=False, textprops={'color': 'white'}, colors=colors, counterclock=False, shadow=True, labels=labels, labeldistance=1.05, autopct='%1.1f%%', startangle=90, center=(0, 0), normalize=None)
