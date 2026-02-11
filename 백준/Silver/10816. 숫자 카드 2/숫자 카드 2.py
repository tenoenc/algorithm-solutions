from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def bsearch(arr, n):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur + step] <= n:
            cur += step
        step //= 2
    return cur

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
cards.sort()
result = []
for n in targets:
    result.append(bisect_right(cards, n) - bisect_left(cards, n))
print(*result)