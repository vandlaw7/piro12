ps_raw = input()
ps = [p for p in ps_raw]

'''code from 3.py'''
def arrange(ps):
    newps = [value for index, value in enumerate(ps) if
             not ((ps[index] == '(' and ps[index + 1] == ')') or (ps[index - 1] == '(' and ps[index] == ')'))]
    return newps

def if_vps(ps):
    # print(ps)
    # initial screen
    if len(ps) == 0:
        return True
    elif len(ps) % 2 == 1:
        return False
    elif ps[0] == ')' or ps[-1] == '(':
        return False

    while arrange(ps) != ps:
        # first screen
        if len(ps) == 0:
            return True
        elif len(ps) % 2 == 1:
            return False
        elif ps[0] == ')' or ps[-1] == '(':
            return False

        ps = arrange(ps)

        # second screen
        if len(ps) == 0:
            return True
        elif len(ps) % 2 == 1:
            return False
        elif ps[0] == ')' or ps[-1] == '(':
            return False



''' main code start'''


def pair_check(string):
    left = 0
    right = 0
    for i in string:
        if i == "(":
            left += 1
        else:
            right += 1

    if left == right:
        return True
    else:
        return False


def reverse(ps):
    list = []
    for p in ps:
        if p == '(':
            list.append(')')
        else:
            list.append('(')
    return list


def solution(ps):

    # 1
    if not ps:
        return []

    # 2
    for i in range(1, len(ps), 2):
        if i == len(ps) - 1:
            u = ps
            v = []
            break

        if pair_check(ps[0:i]) and not pair_check(ps[0:i+2]):
            u = ps[:i]
            v = ps[i+1:]
            # print(u)
            # print(v)
            break

    # 3
    if if_vps(u):
        return u + solution(v)
    else:
    # 4
        # print(u[1:-1])
        return ['('] + solution(v) + [')'] + reverse(u[1:len(u)-2])


print_result = "".join(solution(ps))

print(print_result)