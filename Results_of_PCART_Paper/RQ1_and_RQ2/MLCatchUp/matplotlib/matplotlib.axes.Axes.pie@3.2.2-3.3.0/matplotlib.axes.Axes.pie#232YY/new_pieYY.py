import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, center=(0, 0), colors=colors, textprops={'color': 'white'}, radius=False, counterclock=False, pctdistance=0.85, startangle=90, wedgeprops={'edgecolor': 'black'}, labeldistance=1.05, data=None, autopct='%1.1f%%', shadow=True, normalize=None)
