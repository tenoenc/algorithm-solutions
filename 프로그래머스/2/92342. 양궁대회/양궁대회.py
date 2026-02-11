from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    candidates = []
    max_diff = 0
    for comb in combinations_with_replacement(range(11), n):
        a_score = 0
        l_score = 0
        lion_info = [0] * 11
        for i in comb:
            lion_info[i] += 1
        for i in range(10):
            if info[i] == 0 and lion_info[i] == 0:
                continue
            if info[i] >= lion_info[i]:
                a_score += (10 - i)
            else:
                l_score += (10 - i)
        diff = l_score - a_score
        if diff > 0 and diff >= max_diff:
            if diff > max_diff:
                candidates = []
            max_diff = diff
            candidates.append(lion_info)
    
    if candidates:
        return max(candidates, key=lambda x: x[::-1])
    else:
        return [-1]
