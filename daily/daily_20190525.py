# given an array of integers
# all numbers repeated 3 times expect 1
# find the 1

# implementation 1 : use mod 3
INT_SIZE = 32
def get_single(arr, n):
    result = 0
    # iterate through every bit used for storing integers
    for i in range(0, INT_SIZE):
        # find the sum of all bits at position i
        sm = 0
        x = (1 << i)
        for j in range(0, n):
            if (arr[j] & x):
                sm = sm + 1
        # bits where the sum does not equal 3 make up the single number
        if (sm % 3):
            result = result | x
    return result

# implementation 2 : use maths
def get_single2(arr):
    return (3 * sum(set(arr)) - sum(arr)) / 2

if __name__ == "__main__":
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7] 
    n = len(arr) 
    print(f"The element with single occurrence is {get_single(arr, n)}") 
    print(f"The element with single occurrence is {get_single2(arr)}") 

