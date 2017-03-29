from itertools import takewhile
nums = [2, 4, 6, 7, 8, 9, 10]
a = takewhile(lambda x: x%2==0, nums)
print(list(a))
