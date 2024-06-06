import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(pctdistance=0.6, labels=['A', 'B', 'C', 'D'], x=x, frame=False, counterclock=True, radius=1, normalize=True, wedgeprops=None, explode=None, textprops=None, startangle=90, autopct='%1.1f%%', center=(0, 0), shadow=False, labeldistance=1.1, colors=None, hatch=None)
