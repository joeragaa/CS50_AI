def transpose(board):
    trans = [list(x) for x in list(zip(*board))]
    return trans

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
st = transpose(s)
d1 = [s[0][0], s[1][1], s[2][2]]
d2 = [s[0][2], s[1][1], s[2][0]]
fixed = [x for x in (s + st + [d1] + [d2]) if sum(x) == 15]
