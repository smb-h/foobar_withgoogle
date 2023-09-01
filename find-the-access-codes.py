# python 2.7.13


def make_dividable_list(l):
    print("======================")
    res = {}
    for index, item in enumerate(l):
        if index >= 1 and l[index] == l[index-1]:
            res[item].add(item)
        else:
            res[item] = set()
            for jtem in l[index+1:]:
                print(res)
                if jtem % item == 0:
                    res[item].add(jtem)
    print(res)
    return res

def make_dividable_list2(l):
    print("======================")
    res = {}
    for index, item in enumerate(l):
        res[index] = set()
        for jndex, jtem in enumerate(l[index+1:]):
            print(res)
            if jtem % item == 0:
                res[index].add(jndex + index + 1)
    print(res)
    return res

def solution(l):
    res = make_dividable_list2(l)
    counter = 0
    for index, item in enumerate(l):
        for jtem in res[index]:
            counter += len(res[jtem])
    return counter

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))
print(solution([1, 1, 1, 2, 2, 2, 3, 3, 3, 6]))
print(solution([2, 3, 5]))
print(solution([1, 1, 1, 1]))
