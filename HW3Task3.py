A = int(input())

if A == 0:
    print("error")
else:
    for i in range(A):
        print('%s%s' % (' ' * (A-i-1), '@' * (i*2+1)))

