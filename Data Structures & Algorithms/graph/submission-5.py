class Graph:
    
    def __init__(self):
        self.edges = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.edges[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.edges[src]:
            self.edges[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(f: int, t: int) -> bool:
            if f == dst:
                return True
            if f in visited:
                return False
            visited.add(f)
            for d in self.edges[f]:
                if dfs(d, t):
                    return True
            return False
        return dfs(src, dst)
