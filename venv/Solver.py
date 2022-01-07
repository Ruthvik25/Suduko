board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


visited_sub = [[0 for i in range(cols)] for j in range(rows)]
visited_row = [[0 for i in range(cols)] for j in range(rows)]
visited_col = [[0 for i in range(cols)] for j in range(rows)]


def fun(i, j):
    if i < 3 and j < 3:
        return 0
    elif i < 3 and j < 6:
        return 1
    elif i < 3 and j < 9:
        return 2
    elif i < 6 and j < 3:
        return 3
    elif i < 6 and j < 6:
        return 4
    elif i < 6 and j < 9:
        return 5
    elif i < 9 and j < 3:
        return 6
    elif i < 9 and j < 6:
        return 7
    return 8


def check(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return False
    return True


def rec(i, j):
    if (check(board)):
        return True

    if (j >= 9):
        j = 0
        i = i + 1
    if (i >= 9):
        return False

    if board[i][j] != 0:
        return rec(i, j+1)

    for k in range(1, 10):
        if visited_sub[fun(i, j)][k] != 1 and visited_row[i][k] != 1 and visited_col[j][k] != 1:
            visited_sub[fun(i, j)][k] = 1
            visited_row[i][k] = 1
            visited_col[j][k] = 1
            board[i][j] = k
            if rec(i, j):
                return True
            visited_sub[fun(i, j)][k] = 0
            visited_row[i][k] = 0
            visited_col[j][k] = 0
            board[i][j] = 0


for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            curr = board[i][j]
            visited_sub[fun(i, j)][curr] = 1
            visited_row[i][curr] = 1
            visited_col[j][curr] = 1

ans = rec(0, 0)
print(ans)
if ans:
    for i in range(9):
        print(board[i])