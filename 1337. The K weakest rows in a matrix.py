def k_weakest_row(mat, k):
    count = 0
    row_c = {}

    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                count += 1
        row_c[i] = count
    row_c = [k for k, v in sorted(row_c.items(), key=lambda item: item[1])]
    return row_c[:k]

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
r_value = k_weakest_row(mat, k)
print(r_value)