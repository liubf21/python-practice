
maxn = 20
cur = 0
num = [0] * (maxn)
tree = [0] * (4 * maxn)

def push_up(rt: int):
    tree[rt] = tree[rt * 2] + tree[rt * 2 + 1]

def build(l: int, r: int, rt: int): # rt start from 1
    global cur
    if l == r:
        tree[rt] = num[cur]
        cur += 1
        return
    mid = (l + r) // 2
    build(l, mid, rt * 2)
    build(mid + 1, r, rt * 2 + 1)
    push_up(rt)

def query(ql: int, qr: int, l: int, r: int, rt: int) -> int: # ql and qr don't change in recursion
    if ql <= l and qr >= r:
        return tree[rt]
    mid = (l + r) // 2
    res = 0
    if ql <= mid:
        res += query(ql, qr, l, mid, rt * 2)
    if qr > mid:
        res += query(ql, qr, mid + 1, r, rt * 2 + 1)
    return res

def update(q: int, v: int, l: int, r: int, rt: int):
    if l == r:
        tree[rt] = v
        return
    mid = (l + r) // 2
    if q <= mid:
        update(q, v, l, mid, rt * 2)
    else:
        update(q, v, mid + 1, r, rt * 2 + 1)
    push_up(rt)

if __name__ == "__main__":
    num = [1, 8, 3, 4, 7, 1, 6, 2]
    n = len(num)
    build(1, n, 1)
    print("tree:", tree)
    print(query(1, 3, 1, n, 1))
    print(query(3, 8, 1, n, 1))
    update(3, 10, 1, n, 1)
    print(query(1, 3, 1, n, 1))