# Segregate an array
# only allowed to swap characters
# also known as the "dutch national flag" problem

# start with lo and mid as 0
# swap Rs to the left side and Bs to the right side 
# Gs will naturally end up in the middle

#a = ['R', 'B', 'B', 'G', 'R', 'G', 'B', 'R', 'R', 'B', 'B', 'G', 'R', 'G', 'B', 'R']
a = ['G', 'B', 'R']

def sort_RGB(a: [], arr_size: int) -> []:
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 'R':
            a[lo], a[mid] = a[mid], a[lo]
            lo += 1
            mid += 1
        elif a[mid] == 'G':
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi -= 1
        print(f'{a} lo={lo} mid={mid} hi={hi}')
    return a

print(a)
print(sort_RGB(a, len(a)))