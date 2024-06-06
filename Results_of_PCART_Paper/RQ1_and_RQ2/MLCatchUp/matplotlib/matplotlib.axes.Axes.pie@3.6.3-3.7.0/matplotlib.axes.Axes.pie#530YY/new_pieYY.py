import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, pctdistance=0.6, center=(0, 0), counterclock=True, normalize=True, wedgeprops=None, textprops=None, autopct='%1.1f%%', radius=1, colors=None, startangle=90, frame=False, shadow=False, labels=['A', 'B', 'C', 'D'], labeldistance=1.1, hatch=None)
