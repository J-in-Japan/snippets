# find the minimum itinerary visiting all locations

# flight_list = [
#     ['A', 'B'],
#     ['C', 'B'],
#     ['B', 'A'],
# #    ['', ''],
# #    ['', ''],
# ]

# flight_list = [
#     ['SFO', 'HKO'], 
#     ['YYZ', 'SFO'], 
#     ['YUL', 'YYZ'], 
#     ['HKO', 'ORD'],
# ]

flight_list = [
    ['A', 'B'], 
    ['A', 'C'], 
    ['B', 'C'], 
    ['C', 'A'],
]

starting = 'C'
#starting = 'YUL'
itinerary = []

def find_route(flights, start, itin):
    print(f'Now at: {start}')
    for f in flights:
        if f[0] == start:
            flights2 = flights.copy()
            flights2.remove(f)
            itin.append(f[0])
            if flights2:
                find_route(flights2, f[1], itin)
            itin.append(f[1])
            print(f"found an itinerary: {itin}")
#    print(f"exit itinerary: {itin}")

find_route(flight_list, starting, itinerary)



# start at C
# all the places you can go in X trips
#      A     B     C
# 1    x     1     x
# 2    
# Recursive function
# where can you go next

# build a tree (graph)
# find minimum height (path) visiting all nodes

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

# starting point to next (multiple)

# find all unused with starting point, then compute all destinations