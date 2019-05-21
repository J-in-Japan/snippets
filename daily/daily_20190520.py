import math

value_stream = [2,1,5,7,11,3,3,7,12,1]

sorted = list()
print(sorted)

i = 0
for v in value_stream:
    sorted.insert(i, v)
    sorted.sort()
    median = None
    if len(sorted) == 1:
        meidan = sorted[0]
    elif len(sorted) == 2:
        median = (sorted[0] + sorted[1]) / 2
    elif len(sorted) == 3:
        median = sorted[1]
    else:
        med_pos = math.floor(len(sorted) / 2)
        median = (sorted[med_pos-1] + sorted[med_pos]) / 2
    print(sorted)
    print(f'median = {median}')