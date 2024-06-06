import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], autopct='%1.1f%%', startangle=90, pctdistance=0.6, normalize=True, radius=1, colors=None, counterclock=True, textprops=None, shadow=False, wedgeprops=None, labeldistance=1.1, hatch=None)
