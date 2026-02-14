import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.make_set(x)
        self.make_set(y)

        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]

        return self.size[px]

    def get_size(self, x):
        return self.size[self.find(x)]

T = int(input())
for _ in range(T):
    F = int(input())
    uf = UnionFind()
    for _ in range(F):
        f1, f2 = input().split()
        result = uf.union(f1, f2)
        print(result)