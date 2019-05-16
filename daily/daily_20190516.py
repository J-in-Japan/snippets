# Given an array of elevation values, determine how much rain could be trapped
# Trapped = higher wall segment on either side

# Brute force, maintain a stack of all the max/min points -> O(n2)

# Dynamic programming approach (below):
# Find increasing max from left and increasing max from right
# Trapped = min (left, right) - height at that point 

# walls = [0, 3, 1, 2]
walls = [0,1,0,2,1,0,1,3,2,1,2,1]

peak_stack = []

from_left = []
from_right = []

# from left
for i in range(len(walls)):
    if i == 0:
        from_left.append(walls[i])
    else:
        if walls[i] <= from_left[i-1]:
            from_left.append(from_left[i-1])
        else:
            from_left.append(walls[i])

#print(from_left)

walls.reverse()

# from right
for i in range(len(walls)):
    if i == 0:
        from_right.append(walls[i])
    else:
        if walls[i] <= from_right[i-1]:
            from_right.append(from_right[i-1])
        else:
            from_right.append(walls[i])

from_right.reverse()
walls.reverse()

print(from_left)
print(from_right)

#answer = []
total_trapped = 0

for i in range(len(walls)):
    trappable = 0
    if from_left[i] > from_right[i]:
        trappable = from_right[i]
    elif from_right[i] > from_left[i]:
        trappable = from_left[i]
    if trappable > walls[i]:
        total_trapped += trappable - walls[i]

print(total_trapped)