classess = [ [13, 15], [11, 13], [4, 7], [1, 5], [3, 6] ]

# construct a action list:
# action[0] -> time of action
# action[1] -> type of action (-1 for finish type, 1 for start type)

actions = []
for cla55 in classess:
    actions.append([cla55[0], 1])
    actions.append([cla55[1], -1])

actions.sort()
# [[2, 1], [3, 1], [4, -1], [4, 1], [6, -1], [7, -1], [11, 1], [13, -1], [13, 1], [15, -1]]

min_classrooms = 0
curr_classrooms = 0

for action in actions:
    curr_classrooms += action[1]

    if curr_classrooms > min_classrooms:
        min_classrooms = curr_classrooms

print(min_classrooms)