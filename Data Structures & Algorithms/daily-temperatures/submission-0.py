class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output= [0,]*len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((index, temp))
            else:
                while stack[-1][1]<temp:
                    output[stack[-1][0]] = index - stack[-1][0]
                    stack.pop()
                    if not stack: break
                stack.append((index, temp))
        for index, temp in stack:
            output[index] = 0
        return output
        