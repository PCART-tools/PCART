import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, shadow=False, labels=['A', 'B', 'C', 'D'], pctdistance=0.6, textprops=None, wedgeprops=None, radius=1, counterclock=True, autopct='%1.1f%%', center=(0, 0), normalize=True, colors=None, startangle=90, labeldistance=1.1, hatch=None)
