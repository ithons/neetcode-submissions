def evalRPNrec(tokens, index):
    operands = {'+', '-', '*', '/'}
    last = tokens[index]
    
    if last in operands:
        if tokens[index-1] in operands:
            a, next_index = evalRPNrec(tokens, index-1)
            if tokens[next_index] in operands: b, next_index = evalRPNrec(tokens, next_index)
            else:
                b = int(tokens[next_index])
                next_index -= 1
        else:
            a = int(tokens[index-1])
            if tokens[index-2] in operands: b, next_index = evalRPNrec(tokens, index-2)
            else:
                b = int(tokens[index-2])
                next_index = index - 3
        
        

        match last:
            case '+':
                total = b+a
                print(b, "+", a, "=", total)
            case '-':
                total = b-a
                print(b, "-", a, "=", total)
            case '*':
                total = b*a
                print(b, "*", a, "=", total)
            case '/':
                total = int(b/a)
                print(b, "/", a, "=", total)

    else:
        total = int(last)
        next_index = index - 1
        print("single token ", total)
    return total, next_index

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total, index = evalRPNrec(tokens, len(tokens)-1)
        return total
