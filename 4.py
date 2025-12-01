a1 = ['a', 'c', 'e', 'g']
a2 = ['b', 'd', 'f', 'h']
b1 = ['1', '3', '5', '7']
b2 = ['2', '4', '6', '8']
s = input()
if s[0] in a1:
    if s[1] in b1:
        print('черный')
    else:
        print('белый')
else:
    if s[1] in b2:
        print('черный')
    else:
        print('белый')