N, K, M = map(int, input().split())
ost = N % K
if ost == 0:
    print((N//K)*2*M)
else:
    print((N//K+1)*2*M)