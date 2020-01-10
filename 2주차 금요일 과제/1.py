nstring = input("input integer: " )
decn = len(nstring)
n = int(nstring)


def create(m):
    dec = 10
    list=[]
    while dec <= m :
        list.append(m%10)
        dec *= 10
        if dec == m:
            return m+1
    return m + sum(list)
    
for i in range(n-(decn*9),n):
    if create(i) == n:
        print(i)
        break
    if i == (n-3):
        print(0)