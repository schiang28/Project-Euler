def fractionToDecimal(numr, denr):
    res = ""
    mp = {}
    rem = numr % denr
    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // denr
        res += str(res_part)
        rem = rem % denr
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]
 

numr = 1
recur = 1
for i in range(2,1000):
    res = fractionToDecimal(numr, i)
    if len(res) > recur:
        recur = i

print(recur)