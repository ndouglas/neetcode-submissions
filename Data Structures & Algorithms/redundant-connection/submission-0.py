class UnionFind:

    def __init__(self):
        self.parent = {}
        self.size = {}
        self.num_components = 0

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            x = self.parent[x]
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        elif self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = self.parent[root_y]
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = self.parent[root_x]
            self.size[root_y] += self.size[root_x]
            self.num_components -= 1
        return True

    def add_component(self, x: int):
        if self.has_component(x):
            return
        self.parent[x] = x
        self.size[x] = 0

    def has_component(self, x: int) -> bool:
        return x in self.parent

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind()
        for [x, y] in edges:
            union_find.add_component(x)
            union_find.add_component(y)
            if not union_find.union(x, y):
                return [x, y]
