import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(normalize=True, data=None, pctdistance=0.6, startangle=90, radius=1, colors=None, explode=None, autopct='%1.1f%%', shadow=False, labeldistance=1.1, labels=['A', 'B', 'C', 'D'], x=x, hatch=None)
