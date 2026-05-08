def solution(signals):
    answer = -1
    for i in range(1, 3200001):
        all_yellow = True
        for g, y, r in signals:
            if not (g < ((i-1) % (g + y + r)) + 1 <= g + y):
                all_yellow = False
        if all_yellow:
            answer = i
            break
    return answer