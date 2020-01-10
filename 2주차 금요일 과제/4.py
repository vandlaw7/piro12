string = input()
s = [c for c in string]


def find_divisor(n):
    list=[]
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list


def consec_index(i, k):
    list=[]
    for j in range(k):
        list.append(i+j)
    return list


def string_slice(string, index_list):
    son_string = ""
    for i in index_list:
        son_string += (string[i])
    return son_string


def solution(string):
    divisor_list = find_divisor(len(string))
    result_list = []
    for d in divisor_list:
        piece_list = []
        for i in range(0, len(string), d):
            piece_list.append(string_slice(string, consec_index(i, d)))

        piece_dict = {}
        piece_dict[0] = 1
        for i in range(1, len(piece_list)):
            j = 0
            for k in range(i-1, 0, -1):
                if k in piece_dict:
                    j = k
                    break

            if piece_list[j] == piece_list[i]:
                piece_dict[j] += 1
            else:
                piece_dict[i] = 1

        letter_count = 0
        for key, value in piece_dict.items():
            if value == 1:
                letter_count += d
            else:
                letter_count += (d+1)
        result_list.append(letter_count)
    return min(result_list)


print(solution(string))

