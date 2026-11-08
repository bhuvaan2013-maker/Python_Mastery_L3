
from school import matrix_multiplication

r1, c1 = map(int, input().split())
P = []

for i in range(r1):
    row = list(map(int, input().split()))
    P.append(row)

r2, c2 = map(int, input().split())
Q = []

for i in range(r2):
    row = list(map(int, input().split()))
    Q.append(row)

result = matrix_multiplication(P, Q)

for row in result:
    print(*row)
