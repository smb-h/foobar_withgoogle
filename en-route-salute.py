# python 2.7.13


def solution(s):
    salute_counter = 0
    # all < indices
    lt_indices = [i for i, x in enumerate(s) if x == '<']
    # all > indices
    gt_indices = [i for i, x in enumerate(s) if x == '>']
    for index in lt_indices:
        # count indices of gt_indices that are less than index
        this_gt = [i for i, x in enumerate(gt_indices) if x < index]
        salute_counter += len(this_gt) * 2
    return salute_counter
    
    

print(solution("--->-><-><-->-"))
# 10
print(solution(">----<"))
# 2
print(solution("<<>><"))
# 4
