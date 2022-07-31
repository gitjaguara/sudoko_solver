from pprint import pprint
rows, cols = (9, 9)
sud_mtx = [[0] * cols] * rows
gm = [
    [0, 7, 0, 0, 2, 0, 0, 4, 6],
    [0, 6, 0, 0, 0, 0, 8, 9, 0],
    [2, 0, 0, 8, 0, 0, 7, 1, 5],
    [0, 8, 4, 0, 9, 7, 0, 0, 0],
    [7, 1, 0, 0, 0, 0, 0, 5, 9],
    [0, 0, 0, 1, 3, 0, 4, 8, 0],
    [6, 9, 7, 0, 0, 2, 0, 0, 8],
    [0, 5, 8, 0, 0, 0, 0, 6, 0],
    [4, 3, 0, 0, 8, 0, 0, 7, 0]
]

sz = 3
static_set = set(range(1, sz * sz + 1))
l = sz*sz

def get_row_set(mtx, r, c):
    cr = mtx[r][c]
    rs = set(mtx[r]) - {cr} - {0}
    return rs


def get_col_set(mtx, r, c):
    cr = mtx[r][c]
    cs = set(mtx[c]) - {cr} - {0}
    return cs


def get_squ_set(mtx, r, c):
    cr = mtx[r][c]
    # 1,4
    start_r, end_r = r//sz, (r//sz)+sz  # extra for the range fuinc below
    start_c, end_c = c//sz, (c//sz)+sz
    x = set()
    for i in range(start_r, end_r):
        for j in range(start_c, end_c):
            x.add(mtx[i][j])
    cs = x - {cr} - {0}
    return cs

# print(gm[0][7])
print(static_set)
# print(sud_mtx)
mc = 0
added = True
while added:
    added = False
    mc = mc + 1
    print("Cycle {0}".format(mc))
    for i in range(0, l):
        for j in range(0, l):
            if not gm[i][j]:
                rowset = get_row_set(gm, i, j)
                colset = get_col_set(gm, i, j)
                squset = get_squ_set(gm, i, j)
                res = static_set - (rowset|colset|squset)
                if len(res) == 1:
                    gm[i][j] = list(res)[0]
                    added = True
pprint(gm)
