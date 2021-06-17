with open("/Users/sophiechiang/Downloads/p059_cipher.txt") as f:
    f = list(map(int, f.read().strip().split(",")))


def encryption(a, k):
    e = []
    for i in range(len(a)):
        e.append(chr(a[i] ^ int(k[i % len(k)])))
    return e


a = "".join(encryption(f, [ord("e"), ord("x"), ord("p")]))

ans = 0
for i in a:
    ans += ord(i)

print(ans)