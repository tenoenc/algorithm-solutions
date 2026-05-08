def solution(dist_limit, split_limit):
    answer = 1
    def dfs(nodes, dist, split, leaf):
        nonlocal answer
        if dist > dist_limit:
            return
        answer = max(answer, nodes + leaf)
        for child in range(2, 4):
            nsplit = split * child
            if nsplit > split_limit:
                continue
            new_nodes = nodes * child
            next_nodes = min(new_nodes, dist_limit - dist)
            nleaf =  leaf + (new_nodes - next_nodes)
            dfs(next_nodes, dist + next_nodes, nsplit, nleaf)
        
    dfs(1, 1, 1, 0)
    return answer