from scipy.stats import wilcoxon
x = [12.5, 14.2, 16.8, 18.5, 20.1]
y = [10.9, 13.1, 14.5, 16.2, 19.0]
result = wilcoxon(x=x, alternative='two-sided')
