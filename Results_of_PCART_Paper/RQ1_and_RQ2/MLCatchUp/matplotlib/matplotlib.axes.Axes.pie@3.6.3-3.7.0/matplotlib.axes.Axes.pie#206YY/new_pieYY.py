import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, labeldistance=1.1, normalize=True, labels=['A', 'B', 'C', 'D'], colors=None, shadow=False, autopct='%1.1f%%', pctdistance=0.6, startangle=90, hatch=None)
