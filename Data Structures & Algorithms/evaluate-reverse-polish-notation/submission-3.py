class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ('+', '-', '*', '/')
        stack = []

        for token in tokens:
            x, y = None, None
            if token not in operators:
                stack.append(int(token))
                print(stack)
            elif token in operators:
                y = stack.pop()
                x = stack.pop()
                match token:
                    case '+':
                        stack.append(x + y)
                        print(stack)
                    case '-':
                        stack.append(x - y)
                        print(stack)
                    case '*':
                        stack.append(x * y)
                        print(stack)
                    case '/':
                        stack.append(int(float(x) / y))
                        print(stack)
        
        return stack[-1]
