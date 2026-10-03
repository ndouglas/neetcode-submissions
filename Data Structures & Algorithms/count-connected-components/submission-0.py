class UnionFind:

    def __init__(self, n: int):
        self.parent = {}
        self.size = {}
        self.num_components = 0
        for i in range(n):
            self.insert(i)

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        elif self.size[px] < self.size[py]:
            self.parent[px] = self.parent[py]
            self.size[py] += self.size[px]
        else:
            self.parent[py] = self.parent[px]
            self.size[px] += self.size[py]
        self.num_components -= 1

    def insert(self, x: int):
        self.parent[x] = x
        self.size[x] = 1
        self.num_components += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for [x, y] in edges:
            union_find.union(x, y)
        return union_find.num_components