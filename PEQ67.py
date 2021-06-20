with open("/Users/sophiechiang/Programming/Project Euler/p067_triangle.txt") as f:
    f = f.read().strip().splitlines()

for i in range(len(f)):
    f[i] = list(map(int, f[i].split()))

for row in range(1, len(f)):
    for n in range(len(f[-row - 1])):
        f[-row - 1][n] = max(
            [f[-row][n] + f[-row - 1][n], f[-row][n + 1] + f[-row - 1][n]]
        )

print(f[0])
