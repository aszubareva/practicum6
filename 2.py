A, B = map(int, input().split("x"))
C, D, E = map(int, input().split("x"))
A = min(A, B)
B = max(A, B)
case1 = case2 = case3 = 0
if min(C, D) <= A and max(C, D) <= B:
    case1 = 1
elif min(C, E) <= A and max(C, E) <= B:
    case2 = 1
elif min(D, E) <= A and max(D, E) <= B:
    case3 = 1
if case1 + case2 + case3 != 0:
    print("да")
else:
    print("нет")

