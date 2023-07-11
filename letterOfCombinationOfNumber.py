class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping of digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        self.backtrack('', digits, digit_to_letters, combinations)
        return combinations

    def backtrack(self, combination, remaining_digits, digit_to_letters, combinations):
        # Base case: if there are no remaining digits, add the current combination
        if not remaining_digits:
            combinations.append(combination)
            return
        
        # Get the letters corresponding to the current digit
        current_digit = remaining_digits[0]
        letters = digit_to_letters[current_digit]
        
        # Recursively build combinations for the remaining digits
        for letter in letters:
            self.backtrack(combination + letter, remaining_digits[1:], digit_to_letters, combinations)
digits = "23"
solution = Solution()
result = solution.letterCombinations(digits)
print(result)
