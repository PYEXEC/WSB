class Validator:
    @staticmethod
    def is_valid_parentheses(string: str):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in string:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(Validator.is_valid_parentheses("(){}[]"))
print(Validator.is_valid_parentheses("()[{)}"))
print(Validator.is_valid_parentheses("()"))
