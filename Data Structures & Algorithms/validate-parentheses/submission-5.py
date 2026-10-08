class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketdict = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in bracketdict.keys():
                if len(stack) == 0:
                    return False
                elif stack[-1] == bracketdict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False