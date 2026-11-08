
def matrix_multiplication(P, Q):
    rows_p = len(P)
    cols_p = len(P[0])
    cols_q = len(Q[0])

    result = [[0 for j in range(cols_q)] for i in range(rows_p)]

    for i in range(rows_p):
        for j in range(cols_q):
            for k in range(cols_p):
                result[i][j] += P[i][k] * Q[k][j]

    return result
