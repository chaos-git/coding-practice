def array_left_rotation(a, n, k):
    result = []
    for i in range(len(a)):
        shifted_i = (len(a) + i + k) % len(a)
        result.append(a[shifted_i])
    return result  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str,answer))