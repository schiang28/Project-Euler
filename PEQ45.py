t,p,h= [],[], []

for n in range(143, 100000):
    t.append((n+1)*n/2)
    p.append((3*n-1)*n/2)
    h.append((2*n-1)*n)
    
print(set(t).intersection(p,h))