class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x: int):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(len(accounts))
        email2account = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email2account:
                    union.union(i, email2account[e])
                else:
                    email2account[e] = i
        
        email_group = defaultdict(list)

        for e, i in email2account.items():
            leader = union.find(i)
            email_group[leader].append(e)
        
        result = []

        for i, emails in email_group.items():
            name = accounts[i][0]
            result.append([name] + sorted(email_group[i]))
        
        return result