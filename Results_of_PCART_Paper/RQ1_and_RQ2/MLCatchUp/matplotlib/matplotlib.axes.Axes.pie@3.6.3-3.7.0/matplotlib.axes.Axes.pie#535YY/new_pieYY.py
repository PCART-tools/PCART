import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, startangle=90, shadow=False, counterclock=True, radius=1, autopct='%1.1f%%', labeldistance=1.1, wedgeprops=None, labels=['A', 'B', 'C', 'D'], explode=None, frame=False, data=None, pctdistance=0.6, textprops=None, colors=None, center=(0, 0), hatch=None)
