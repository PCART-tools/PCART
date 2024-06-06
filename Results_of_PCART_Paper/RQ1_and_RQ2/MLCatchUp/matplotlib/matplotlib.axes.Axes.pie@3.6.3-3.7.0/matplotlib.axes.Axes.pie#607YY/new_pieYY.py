import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(center=(0, 0), autopct='%1.1f%%', x=x, frame=False, rotatelabels=False, explode=None, wedgeprops=None, radius=1, colors=None, shadow=False, labels=['A', 'B', 'C', 'D'], startangle=90, textprops=None, pctdistance=0.6, counterclock=True, labeldistance=1.1, data=None, hatch=None)
