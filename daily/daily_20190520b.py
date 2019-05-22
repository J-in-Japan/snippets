# Another attempt at the running median problem
# This time using multisets (aka Counters in python) with pointers to the median(s)

import collections

c = collections.Counter()
p_hi = None
p_lo = None

value_stream = [2,1,5,7,11,3,3,7,12,1]

cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
    print(cnt.elements)
    

print('stop')

for n in value_stream:
    
    # if set is empty, just add and assign both pointers
    if len(c) == 0: 
        p_hi = 0
        p_lo = 0
    # if set has odd number, both medians should be pointing at the same element
    elif n & 1:
        if n < c[p_lo]:
            p_lo -= 1 # low pointer moves to the left

# Python counter does not work the same way as c++ 