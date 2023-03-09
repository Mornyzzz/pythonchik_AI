from functools import cache

def lev_rec(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)

    elif a[i - 1] == b[j - 1]:
        return lev_rec(a, b, i - 1, j - 1)

    else:
        return 1 + min(lev_rec(a, b, i, j - 1), lev_rec(a, b, i - 1, j), lev_rec(a, b, i - 1, j - 1))

@cache
def lev_dist(a, b):
    return lev_rec(a, b, len(a), len(b))

print(lev_dist('столб', 'слон'))