# determine if a list of elements can be used to form a given sum

in_s = {10,15,3,7}
in_k = 17

def can_sum_n2(s, k):
    for a in s:
        for b in s:
            print('> ' + str(a) + ':' + str(b))
            if (a != b) and (a+b == k):
                return True
    return False

print(can_sum_n2(in_s, in_k))

def can_sum_n(s, k):
    for a in s:
        print('> ' + str(a) + ':' + str(k-a))
        if (k-a) in s:
            return True
    return False

print(can_sum_n(in_s, in_k))
