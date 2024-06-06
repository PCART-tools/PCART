import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, radius=1, normalize=True, pctdistance=0.6, shadow=False, startangle=90, autopct='%1.1f%%', labeldistance=1.1, labels=['A', 'B', 'C', 'D'], colors=None, hatch=None)
