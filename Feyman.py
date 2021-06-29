def nod(h,y):
    while y > 0:
        d = (h % y)
        h = y
        y = d
    return h    

def frac(h,y):
    return h // nod(h,y)


def sum(num):
    if num == 0:
        return 0 
    else:
        return sum(num-1) + num
    

c = 200



rep = []
imp = []

for t in range(c):
    for x in range(t+1):
        if (x+t)%2 == 0:
            if x == t:
                rep.append(0)
                imp.append(1)
            elif x == 0:
                rep.append(imp[sum(t-1) + x + 1] + rep[sum(t-1) + x + 1])
                imp.append(0)
            elif x == 1:
                imp.append(0)
                rep.append(imp[sum(t-1) + x + 1] + rep[sum(t-1) + x + 1])
            elif True:
                imp.append(imp[sum(t-1) + x - 1] - rep[sum(t-1) + x - 1])
                rep.append(imp[sum(t-1) + x + 1] + rep[sum(t-1) + x + 1])
        else:
            rep.append(0)
            imp.append(0)

s=0
for t in range(1,c):
    
    if (t)%2 == 0:
            f = rep[sum(t)]
            d = (rep[sum(t)]**2 + imp[sum(t)]**2)
            print('p(',0,',',t,') =',  f,'for',2,'^',(t-1))
            s = s + d/(2**(t-1))
print(s)
input('end')
