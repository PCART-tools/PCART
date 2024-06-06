from scipy.stats import mood
x = [3, 4, 5, 6, 7]
y = [1, 2, 3, 4, 5]
result = mood(x, y, alternative='two-sided')
