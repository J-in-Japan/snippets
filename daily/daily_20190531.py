# given rand5() which returns a random number between 0 and 5 inclusive, implement rand7()

# my solution below works but could be written simpler by just doing 8 * rand5() % 8

import random
import collections

def rand5()->int:
    return random.randint(0, 5)

def rand7()->int:
    # s = rand5()
    # v = (s / 5) * 7
    # print(f'{s} -> {v}')
    # return v
    # starting_index = rand5()
    # increment = rand5()
    # result = starting_index + increment
    result = 0
    for i in range(8):
        result += rand5() 
        if result > 7:
            result -= 8
    return result
    

# print(rand5())
# print(rand5())
# print(rand5())
# print(rand5())
# print(rand5())
# print(rand5())
# print(rand5())
# print(rand5())

# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())
# print(rand7())

# rand7()
# rand7()
# rand7()
# rand7()
# rand7()
# rand7()
# rand7()
# rand7()
# rand7()
# rand7()

c = collections.Counter()
for i in range(1000000):
    c[rand7()] += 1
print(c)
# 0
#   0
# 1
#   1
# 2
#   2
# 3
#   3
# 4
#   4
# 5
#   5
# 6
  
# 7