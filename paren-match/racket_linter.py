class RacketLinter:

    #Problem: Matching Parenthesis Problem Variant
    #Create a Racket linter that checks for matching parenthesis in Racket code 
    #detects the location of the missing closing character 
    #and returns the line and character number of the opening character
    #Constraints:  parenthesis only includes {'(', ')', '[', ']'}
    parenthesis_pairs = {']': '[', ')': '('} 
    open_parenthesis = ('[', '(')   
    closing_parenthesis = (']', ')')   


    # TODO: figure out how to read through each line of racket code,
    #character by character and store the line number and character number in the line
    # of each character
    # def read_in_racket_code(self, file_name):
    #     line_num = 0
    #     char_num = 0
    #     with open(file_name) as fileobj:
    #         for line in fileobj:  
    #             for ch in line: 
    #                 char_num += 1
    #             line_num += 1        


    #Matching Parenthesis Problem Variant
    #Approach 1:
    #Iterate through each character of racket code
    #if character == '[' or character == '(':
    #   push [character, line no., char no.] onto stack 
    #elif character == ']' or character == ')':
    #   open_paren_line_num_char_num = stack.pop()
    #   open_paren = open_paren_line_num_char_num[0]
    #   if character == ']' and open_paren != '[' or character == ')' and open_paren != '(':
    #       line_num = open_paren_line_num_char_num[1]
    #       char_num = open_paren_line_num_char_num[2]   
    #       return line_num, char_num  
    #else:
    #   continue
    #time: O(n)
    #space: O(n)


    def find_open_parenthesis_to_match_missing_closing_parenthesis(self, file_name):
        stack = []
        
        line_num = 1
        char_num = 0
        with open(file_name) as fileobj:
            for line in fileobj:
                for ch in line: 
                    if ch in self.open_parenthesis:
                        stack.append([ch, line_num, char_num])
                    elif ch in self.closing_parenthesis:
                        open_paren_line_num_char_num = stack.pop()
                        open_paren = open_paren_line_num_char_num[0]
                        if open_paren != self.parenthesis_pairs[ch]:
                            line_num = open_paren_line_num_char_num[1]
                            char_num = open_paren_line_num_char_num[2]
                            return line_num, char_num      
                    char_num += 1
                line_num += 1
                char_num = 0  
        return -1, -1

if __name__== '__main__':
    racketLinter = RacketLinter()

    # racketLinter.read_in_racket_code("stretch.rkt")

    expected_line_and_char_num = 9,5
    actual_line_and_char_num = racketLinter.find_open_parenthesis_to_match_missing_closing_parenthesis("stretch.rkt")
    assert expected_line_and_char_num == actual_line_and_char_num, "failed test case 1 of find_open_parenthesis_to_match_missing_closing_parenthesis"

#   Ex. 1
    # Input: s = "()"
# Output: true
    
#   Ex. 2
#     Input: s = "()[]{}"
# Output: true


#     Example 3:

# Input: s = "(]"
# Output: false
    
    #     Example 4:

# Input: s = "["
# Output: false
    
        #     Example 5:

# Input: s = ")"
# Output: false
    
            #     Example 6:

# Input: s = "({)}"
# Output: false