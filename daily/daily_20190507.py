# Two singly linked lists
# list_a = 7 -> 3 -> 10 -> 8
# list_b = 1 -> 5 -> 2 -> 10 -> 8
# find the intersection point (or return null)

list_a = [7, 3, 10, 8]
list_b = [1, 5, 2, 10, 8]

# my method: convert the list to an array and check backward from the end
#i = 1
#while list_a[-i] == list_b[-i] and i < len(list_a) and i < len(list_b):
#    print(list_a[-i])
#    i = i+1
#print("intersect: ", list_a[-i+1])

# best solution: get the length of each list, ignore the difference from start of longer list, start checking for intersection
len_a = len(list_a)
len_b = len(list_b)
pointer_a = 0
pointer_b = 0
if len_a > len_b:
    pointer_a = len_a - len_b
if len_b > len_a:
    pointer_b = len_b - len_a
while pointer_a < len_a and pointer_b < len_b:
    if list_a[pointer_a] == list_b[pointer_b]:
        print("Intersect: ", list_a[pointer_a])
        break
    pointer_a = pointer_a + 1
    pointer_b = pointer_b + 1
print("end")