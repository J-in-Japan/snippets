# given schedule (start, end) find minimum required rooms

# my idea: sort by end time

class lecture:
    start = 0
    end = 0
    duration = 0
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.duration = e - s
    def __str__(self):
        return "s:" + str(self.start) + " e:" + str(self.end)

# sort by earliest end time
# keep adding meetings, if cannot add then extra room needed

lectures = [lecture(1, 3), lecture(4, 5), lecture(1, 2)]
#print(lectures)
for l in lectures:
    print(l)

lectures.sort(key=lambda lecture: lecture.start)

for l in lectures:
    print(l)

# if lectures is not empty
room_count = 1
current_count = 1
for i in range(len(lectures)):
    if i > 0:
        if lectures[i].start < lectures[i-1].end:
            current_count = current_count + 1
            if current_count > room_count:
                room_count = current_count
        else:
            current_count = 1
print(room_count)

# assign meetings to room(s)
#rooms = []

