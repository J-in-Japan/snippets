# playing around with built-in python functions for processing sequences

# map
# apply a function to each element in the iterable
map( int, [ "10", "12", "14", 3.1415926, "5L" ] )
# >> [10, 12, 14, 3, 5]


# reduce
# apply a function to each element in the iterable to generate a cumulative result (can also supply an initial value)
#import functools
import functools
def add(a,b):
    return a+b
functools.reduce( add, range(10) )
# >> 45


# filter
# chooses elements from the iterable where a filter condition is true
def gt2( a ):
    return a > 2
filter( gt2, range(8) )
# >> [3, 4, 5, 6, 7]
def div3( a ):
    return a % 3 == 0
filter( div3, range(10) )
# >> [0, 3, 6, 9]


# zip
# iterates values of two (or more) sequences to create a new sequence
zip( range(5), range(1,20,2) )
# >> [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9)]

x = range(1, 20, 2)
for y in x:
    print(y)

