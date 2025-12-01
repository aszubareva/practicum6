K = int(input())
m1 = K//7 +1
m2 = K//5 + 1
flag = 0
for i in range(m1):
    for j in range(m2):
        if i*7+j*5 == K:
            print('да')
            flag = 1
            break
    if flag == 1:
        break
if flag == 0:
    print('нет')