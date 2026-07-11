class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            print(stack)
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(a-b)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(int(a/b))
            else: stack.append(int(token))
                
        return stack[-1]