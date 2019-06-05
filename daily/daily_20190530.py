# Given an array of integers, identify any inversions
# inversion: A[i] > A[j] when i < j

a = [2, 4, 1, 3, 5]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            print(f'Inversion: ({a[i]},{a[j]})')
