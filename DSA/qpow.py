
def qpow(x: int, n: int):
    res = 1
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

def qpow_mod(x: int, n: int, mod: int):
    res = 1
    while n:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

if __name__ == "__main__":
    assert qpow(2, 10) == 1024
    assert qpow(3, 5) == 243