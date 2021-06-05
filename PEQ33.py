for a in range(10,100):
    for b in range(10,100):
        if a<b and a%10 != 0 and b%10 != 0:
            x = a/b
            for i in range(2):
                if str(a)[i] in str(b):
                    n,d = str(a)[1-i], str(b)[1-str(b).index(str(a)[i])]
                    if int(n)/int(d) == x:
                        print(a,b,x)
                        break