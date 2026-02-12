from queue import deque

T = int(input())
for _ in range(T):
    commands = input()
    N = int(input())
    arr_str = input()[1:-1]
    
    if N == 0:
        dq = deque()
    else:
        dq = deque(arr_str.split(","))

    reverse = False
    error = False

    for command in commands:
        if command == "R":
            reverse = not reverse
        else:
            if not dq:
                error = True
                break
            if reverse:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print("error")
    else:
        if reverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")