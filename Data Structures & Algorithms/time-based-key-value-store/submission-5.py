class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        table = self.table[key]
        result = ""
        if not table:
            return result
        lp, rp = 0, len(table) - 1
        if rp < lp:
            return result
        if table[lp][0] > timestamp:
            return result
        while lp <= rp:
            mp = lp + (rp - lp) // 2
            me = table[mp]
            if me[0] <= timestamp:
                result = me[1]
                lp = mp + 1
            else:
                rp = mp - 1
        return result