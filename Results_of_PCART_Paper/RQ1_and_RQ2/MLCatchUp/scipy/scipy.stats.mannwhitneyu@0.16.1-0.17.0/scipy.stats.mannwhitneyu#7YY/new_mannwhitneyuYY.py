import scipy.stats as stats
result = stats.mannwhitneyu(x=[1, 2, 3, 4, 5], y=[6, 7, 8, 9, 10], use_continuity=True, alternative='two-sided')
