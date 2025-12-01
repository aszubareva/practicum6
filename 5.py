s = input()
c1 = abs(ord(s[0]) - ord(s[3]))
c2 = abs(ord(s[1]) - ord(s[4]))
if (c1 == 2 and c2 == 1) or (c1 == 1 and c2 == 2):
    print('верно')
else:
    print('ошибка')