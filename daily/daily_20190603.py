import collections

arr = [34, -50, 42, 14, -5, 86]
ans = 137

max_so_far = 0
max_ending_here = 0
for i in range(len(arr)):
    max_ending_here += arr[i]
    if max_ending_here < 0:
        max_ending_here = 0
    elif max_so_far < max_ending_here:
        max_so_far = max_ending_here
print(f'max sum = {max_so_far}')
assert max_so_far == ans

# while there are negative numbers in the deck
# if the numbers outside are larger than the negative, and there are more positives on the other side, then we can keep the negative

# go through once from the left and then once from the right

# 0
# 34 -50 42




# 34
# -16
# 26    
# 40    95
# 35    81
# 111   86