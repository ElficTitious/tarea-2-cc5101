from math import ceil, floor, log2

def a_n(n : int) -> int:
    if n == 0 or n == 1:
        return n

    return (2*n - 1) + a_n(ceil((n - 1)/2)) + a_n(floor((n - 1)/2))

def b_n(n : int) -> int:
    if n == 0 or n == 1:
        return n
    
    return n + b_n(ceil(n/2)) + b_n(floor(n/2))

def sol_a_n(n: int) -> int:
    return n + 2 * (floor(log2(n)) * (n + 1) + 2 * (1 - 2 ** floor(log2(n))))

def sol_b_n(n: int) -> int:
    return n * ceil(log2(n)) + 2 * n - 2 ** ceil(log2(n))

def c_n(n: int) -> float:
    return sol_a_n(n) / sol_b_n(n)

def d_n(n : int) -> int:
    if n == 0:
        return 1
    
    return 2 + d_n(floor((n - 1)/2))