letter_map = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z'],
]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGITS = len(digits)
        result = []
        working = []
        def backtrack(index: int):
            if index == DIGITS:
                if len(working):
                    result.append(''.join(working))
                return
            number = int(digits[index])
            letters = letter_map[number - 2]
            for letter in letters:
                working.append(letter)
                backtrack(index + 1)
                working.pop()
        backtrack(0)
        return result