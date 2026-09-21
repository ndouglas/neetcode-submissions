from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        finishable = set()
        visited = set()

        def dfs(start: int) -> bool:
            if start in finishable:
                return True
            if not len(adj_list[start]):
                finishable.add(start)
                return True
            if start in visited:
                return False
            result = True
            visited.add(start)
            for prereq in adj_list[start]:
                result = result and dfs(prereq)
            visited.remove(start)
            if result:
                finishable.add(start)
            return result

        for i in range(len(prerequisites)):
            adj_list[prerequisites[i][0]].append(prerequisites[i][1])

        for i in range(numCourses):
            if i not in finishable and not dfs(i):
                return False

        return True
