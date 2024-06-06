import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x=x, normalize=True, labels=['A', 'B', 'C', 'D'], pctdistance=0.6, autopct='%1.1f%%', shadow=False, data=None, explode=None, startangle=90, labeldistance=1.1, colors=None, hatch=None)
