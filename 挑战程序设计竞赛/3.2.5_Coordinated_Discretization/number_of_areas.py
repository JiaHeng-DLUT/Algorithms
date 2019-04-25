# -*- coding: utf-8 -*-
"""
@author: jiaheng
@time: 9/13/2018
@version: 1.0
"""


# input
MAX_N = 100
(W, H, N) = (10, 10, 5)
X1 = [1, 1, 4, 9, 10]
X2 = [6, 10, 4, 9, 10]
Y1 = [4, 8, 1, 1, 6]
Y2 = [4, 8, 10, 5, 10]
fld = [[0 for i in range(MAX_N * 6)] for i in range(MAX_N * 6)]


def compress(x1, x2, w):
    result = [1] * (w + 1)
    for i in range(0, N):
        if x1[i] - 1 >= 1:
            if result[x1[i] - 1] == result[x1[i]]:
                for j in range(x1[i], w + 1):
                    result[j] += 1
        if x2[i] + 1 <= w:
            if result[x2[i]] == result[x2[i] + 1]:
                for j in range(x2[i] + 1, w + 1):
                    result[j] += 1
    # update list
    for j in range(0, N):
        x1[j] = result[x1[j]]
        x2[j] = result[x2[j]]
    return result[w]


def solve():
    # compress
    global W, H
    W = compress(X1, X2, W)
    H = compress(Y1, Y2, H)
    # fill
    for i in range(0, N):
        for y in range(Y1[i], Y2[i] + 1):
            for x in range(X1[i], X2[i] + 1):
                fld[y][x] = 1
    # calculate
    ans = 0
    list1 = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for y in range(1, H + 1):
        for x in range(1, W + 1):
            if fld[y][x]:
                continue
            ans += 1
            fld[y][x] = 1
            # bfs
            list1.append([x, y])
            while list1:
                temp = list1.pop(0)
                (sx, sy) = (temp[0], temp[1])
                for i in range(0, 4):
                    (tx, ty) = (sx + dx[i], sy + dy[i])
                    if tx <= 0 or W < tx or ty <= 0 or H < ty:
                        continue
                    if fld[ty][tx]:
                        continue
                    list1.append([tx, ty])
                    fld[ty][tx] = 1
    # output
    print(ans)


def main():
    solve()


if __name__ == "__main__":
    main()
