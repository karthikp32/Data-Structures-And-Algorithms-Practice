class BasicCalculator:

 

    #output: 1
    # what are implicit parenthesis? does that process the arithmetic expression 
    # so it follows PEMDAS (Parenthesis, Exponent, Multiply/Divide, Add/Subtract)
    # what is the range of numbers? will they be only ints or can they be floating point numbers?
    # is it guaranteed the inputs will be valid arithmetic expression? will there be negative numbers?
    # Ex.2
    # input: "(4 + (8/2))"
    # output: 8
    # Ex.2
    # input: "(4 - (8/2))"
    # output: 0
    # input: "(4 - (-8 / 2))"
    # output: 8
    # input: "(134 / 13))"
    # output: 10
    # input: "(134 / 13 + 3) + 7)"
    # output: 20
    #Constraints: 
    #numbers will only be integers
    #numbers can be negative
    #inputs will be valid arithmetic expression
    #won't have ^

        #input: "(1 + (1-1))"
    #can be represented hierarchically in a tree
    #           (1 + (1-1))
    #               | 
    #               +
    #           1       -
    #                 1     1   

    #Approach 1: Iterative
    #operators = ['+', '-', '*', '/]
    #math_expr_stack = []
    #   curr_operator = '+'
    #iterate one char at a time
    #for char in expr: 
    #   if char == '(' or char == ' ':
    #       continue 
    #   elif char == ')':
    #       
    #       left = math_expr_stack.pop()
    #       right = curr_num
    #       answer = calculate(left, right, curr_operator)
    #   elif isnumeric(char):  
    #       curr_num += int(char)
    #   elif char in operators:
    #       curr_operator = char
    #       math_expr_stack.append(curr_num)
    #       math_expr_stack.append(curr_operator)
    #       curr_num = 0
          
     


    #def calculate(self, left, right, curr_operator)
    #   if curr_operator == '+':
    #       return left + right
    #   elif curr_operator == '-':
    #       return left - right
    #   elif curr_operator == '*':
    #       return left * right
    #   elif curr_operator == '/':
    #       return left // right

    # TODO: modify approach to account for negative numbers after
    # could treat subtraction as addition of negative numbers


if __name__ == '__main__':
    pass    