class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        map = defaultdict(list)
        for i in range(len(strs)):
            string = strs[i]
            map[''.join(sorted(string))].append(string)
        for k, v in enumerate(map.items()):
            result.append(v[1])
        return result