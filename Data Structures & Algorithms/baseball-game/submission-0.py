class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            match operation:
                case '+':
                    rhs = record[len(record) - 1]
                    lhs = record[len(record) - 2]
                    ans = rhs + lhs
                    record.append(ans)
                case 'C':
                    record.pop()
                case 'D':
                    rhs = record[len(record) - 1]
                    ans = 2 * rhs
                    record.append(ans)
                case _:
                    record.append(int(operation))
        return sum(record)
        

        