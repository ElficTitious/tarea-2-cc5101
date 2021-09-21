from math import log10
from recurrences import *
import numpy as np
import matplotlib.pyplot as plt

def min_exp_of_limit(epsilon: float) -> str:
    N = 1
    curr_c_n = c_n(N)
    while abs(curr_c_n - 2) >= epsilon:
        N *= 10
        curr_c_n = c_n(N)
    
    return log10(N)

    

def main():
    
    exp = 4
    epsilon = 0.1
    while epsilon >= 10 ** -exp:
        N = min_exp_of_limit(epsilon)
        print("Minimo numero N t.q., tomando n = 10**N, se cumple que |c_N - 2| < {0:.1e} es: {1}".format(epsilon, N))
        epsilon /= 10

    nums = np.arange(1, 100_000, 1)
    c_n_arr = np.array([c_n(n) for n in nums])

    plt.clf()
    plt.plot(nums, c_n_arr)
    plt.xlabel("n", fontsize=12)
    plt.ylabel(r"$c_n = \frac{a_n}{b_n}$", fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()