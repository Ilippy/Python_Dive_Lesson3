from collections import Counter

lst = [1, 1, 2, 2, 3, 3]
lst = [key for key, value in Counter(lst).items() if value > 1]
print(lst)