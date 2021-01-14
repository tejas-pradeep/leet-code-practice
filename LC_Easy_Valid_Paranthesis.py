 def isValid(self, s: str) -> bool:
        stack = []
        counterpart = {'}' : '{', ')' : '(', "]": "["}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack == [] or counterpart[i] !=stack.pop():
                    return False
        return stack == []
        