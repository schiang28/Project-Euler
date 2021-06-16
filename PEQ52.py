def permutation(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    return False


n = 10
while True:
    if (
        permutation(n, n * 2)
        and permutation(n, n * 3)
        and permutation(n, n * 4)
        and permutation(n, n * 5)
        and permutation(n, n * 6)
    ):
        print(n)
        break
    n += 1
