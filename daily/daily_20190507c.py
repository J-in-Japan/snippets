# a more efficient approach to the scheduling rooms required problem
# put all the start and end times into an array and sort them
# +1 room for each start and -1 for each end
# max reached is required number of rooms

lectures = [ [13, 15], [11, 13], [4, 7], [1, 5], [3, 6] ]

# construct a action list:
# action[0] -> time of action
# action[1] -> type of action (-1 for finish type, 1 for start type)

actions = []
for lecture in lectures:
    actions.append([lecture[0], 1])
    actions.append([lecture[1], -1])

actions.sort()
# [[2, 1], [3, 1], [4, -1], [4, 1], [6, -1], [7, -1], [11, 1], [13, -1], [13, 1], [15, -1]]

max_rooms = 0
curr_rooms = 0

for action in actions:
    curr_rooms += action[1]

    if curr_rooms > max_rooms:
        max_rooms = curr_rooms

print(max_rooms)