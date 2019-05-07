# different ways to climb a staircase

def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return(1)
    else:
        for x in X:
            sum += staircase(n-x, X)
        return sum

def staircaseb(n):
    a, b = 1, 2
    #b = 2
    for _ in range(n-1):
        a, b = b, a + b
        #b = a + b
    return a

#step_options = {1, 2}

answer = staircase(4, {1, 2})
#answerb = staircaseb(4)

print(answer)
print(answerb)

###
#N = 1: [1] = 1
#N = 2: [1,1][2] = 2
#N = 3: [1,1,1][1,2][2,1] = 3
#N = 4: [1,1,1,1][2,1,1][1,2,1][1,1,2][2,2] = 5
#N = 5: [1,1,1,1,1][2,2,1]  