# given schedule (start, end) find minimum required rooms

# my idea: sort by end time

class lecture:
    start = 0
    end = 0
    duration = 0
    def __init__(self, s, e):
        self.start = s
        self.end = e
        # self.duration = e - s
    def __str__(self):
        return "s:" + str(self.start) + " e:" + str(self.end)

lectures = [lecture(1, 3), lecture(4, 5), lecture(1, 2)]
for l in lectures:
    print(l)

# sort by earliest start time
lectures.sort(key=lambda lecture: lecture.start)
for l in lectures:
    print(l)

# go through the list of active meetings
# if there are not enough rooms available then increase the number of rooms required
room_count = 1 # keep track of the max number of rooms reached
current_count = 1 # keep track of how many are needed during the current interval
for i in range(len(lectures)):
    if i > 0:
        # if the start of this lecture is before the end of the previous one
        if lectures[i].start < lectures[i-1].end:
            # then we need an extra room
            current_count = current_count + 1
            if current_count > room_count:
                room_count = current_count
        else:
            current_count = 1

print(room_count)