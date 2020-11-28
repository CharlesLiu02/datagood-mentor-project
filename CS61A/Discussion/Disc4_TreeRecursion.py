def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
print(count_stair_ways(6))

"""
def count_k(n, k):
    if k > n:
        k = n
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if k == 1:
        return 1
    else:
        return count_k(n - 1, k) + count_k(n - 2, k) + count_k(n - 3, k)

"""

def count_k(n, k):
    if n < 0:
        return 0
    if  n == 0:
        return 1
    else:
        total = 0
        for i in range(1, k+1):
            total += count_k(n - i, k)
        return total
print(count_k(3,3))


"""
def even_weighted(s):
    return x * s[0] in s if x % 2 == 0
x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))
"""
