n = int(input())

def arrange(ps):
    newps = [value for index, value in enumerate(ps) if
             not ((ps[index] == '(' and ps[index + 1] == ')') or (ps[index - 1] == '(' and ps[index] == ')'))]
    return newps

def if_vps(ps):
    # initial screen
    if len (ps) == 0:
        print("YES")
        return

    elif len(ps) % 2 == 1:
        print("NO")
        return
    elif ps[0] == ')' or ps[-1] == '(':
        print("NO")
        return

    while arrange(ps) != ps:
        # first screen
        if len(ps) == 0:
            print("YES")
            return
        elif len(ps) % 2 == 1:
            print("NO")
            return
        elif ps[0] == ')' or ps[-1] == '(':
            print("NO")
            return

        ps = arrange(ps)

        # second screen
        if len(ps) == 0:
            print("YES")
            return
        elif len(ps) & 2 == 1:
            print("NO")
            return
        elif ps[0] == ')' or ps[-1] == '(':
            print("NO")
            return


for i in range(n):
    ps_raw = input()
    ps = [p for p in ps_raw]
    if_vps(ps)












