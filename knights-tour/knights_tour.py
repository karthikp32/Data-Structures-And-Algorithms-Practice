import random

class KnightsTour:

    #Class Chess Problem: Knight's Tour
    #Find a way to land on every square in the chess board precisely once
    #If you find it takes too long to compute this on a regular 8x8 chessboard, 
    #try it with 5x5 first, then try to think of a way to improve your approach to get to an answer sooner.
    #Input: Knight starts on one cell in 5x5 chessboard
    #Output: Knight has traversed every cell in 5x5 chessboard
    #Possible operations: [Different combinations of (1 step up/1 step down and 2 steps to the left/right) or (2 steps up/down and 1 step to the left/right)]
    #Starting state: Knight starts on random cell in 5x5 chessboard
    #Goal state: Knight has traversed every cell in 5x5 chessboard
    #Starting state --> path 1/combinations of states
    #               --> path 2/combinations of states   --> goal state
    #               --> ...
    #               --> path n/combinations of states
    #Approach 1:
    #create list of 8 state_transitions #[(vertical steps, horizontal steps)...] for ex. [(-1, 2)] means one step down and 2 steps to the right
    #generate random state/position from 0,0 to 4,4 and set to starting_position
    #create visited = set()
    #chessboard = [[0 for x in range(5)] for y in range(5)]
    #add starting_position to bfsQ
    #while bfsQ:
    #set curr_position = bfsQ.pop(0)
    #visited.add(curr_position)
    #chessboard[curr_position[0]][curr_position[1]] = 1
    #if len(visited) == 25:
    #   return chessboard
    #for transition in state_transitions:
    #   new_pos_row = curr_position[0] + transition[0]
    #   new_pos_col = curr_position[1] + transition[1]
    #   if ((new_pos_row, new_pos_col) not in visited and (new_pos_row >= 0 and new_pos_row <= 4)
    #       and (new_pos_col >= 0 and new_pos_col <= 4):
    #       bfsQ.append((new_pos_row, new_pos_col))
    #time: O(rc)
    #space: O(rc)

    def find_knights_tour_bfs(self, rows_in_board, cols_in_board):
        state_transitions = [(-1,2), (-1,-2), (1,2), (1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        starting_position = (random.randint(0,rows_in_board - 1), random.randint(0,cols_in_board - 1))
        # starting_position = (0,0)
        visited = set()
        chessboard = [[0 for x in range(rows_in_board)] for y in range(cols_in_board)]
        bfsQ = [starting_position]
        visited.add(starting_position)
        while bfsQ:
            curr_position = bfsQ.pop(0)
            visited.add(curr_position)
            chessboard[curr_position[0]][curr_position[1]] = 1
            if len(visited) == rows_in_board * cols_in_board:
                return chessboard
            for transition in state_transitions:
                new_pos_row = curr_position[0] + transition[0]
                new_pos_col = curr_position[1] + transition[1]              
                if ((new_pos_row, new_pos_col) not in visited) and (new_pos_row >= 0 and new_pos_row <= rows_in_board - 1) and (new_pos_col >= 0 and new_pos_col <= cols_in_board - 1):
                    bfsQ.append((new_pos_row, new_pos_col))
        return chessboard
    
    def find_knights_tour_dfs_iterative(self, rows_in_board, cols_in_board):
        state_transitions = [(-1,2), (-1,-2), (1,2), (1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        starting_position = (random.randint(0,rows_in_board - 1), random.randint(0,cols_in_board - 1))
        # starting_position = (0,0)
        visited = set()
        chessboard = [[0 for x in range(rows_in_board)] for y in range(cols_in_board)]
        dfsStack = [starting_position]
        visited.add(starting_position)
        while dfsStack:
            curr_position = dfsStack.pop()
            visited.add(curr_position)
            chessboard[curr_position[0]][curr_position[1]] = 1
            if len(visited) == rows_in_board * cols_in_board:
                return chessboard
            for transition in state_transitions:
                new_pos_row = curr_position[0] + transition[0]
                new_pos_col = curr_position[1] + transition[1]              
                if ((new_pos_row, new_pos_col) not in visited) and (new_pos_row >= 0 and new_pos_row <= rows_in_board - 1) and (new_pos_col >= 0 and new_pos_col <= cols_in_board - 1):
                    dfsStack.append((new_pos_row, new_pos_col))
        return chessboard
    
    def find_knights_tour_dfs_recursive(self, curr_position, chessboard, visited, rows_in_board, cols_in_board):
        state_transitions = [(-1,2), (-1,-2), (1,2), (1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        visited.add(curr_position)
        if len(visited) != rows_in_board * cols_in_board:
            visited.add(curr_position)
            chessboard[curr_position[0]][curr_position[1]] = 1
            if len(visited) == rows_in_board * cols_in_board:
                return chessboard
            for transition in state_transitions:
                new_pos_row = curr_position[0] + transition[0]
                new_pos_col = curr_position[1] + transition[1]              
                if ((new_pos_row, new_pos_col) not in visited) and (new_pos_row >= 0 and new_pos_row <= rows_in_board - 1) and (new_pos_col >= 0 and new_pos_col <= cols_in_board - 1):
                    return self.find_knights_tour_dfs_recursive((new_pos_row, new_pos_col), chessboard, visited, rows_in_board, cols_in_board)
        return chessboard


    
if __name__ == '__main__':    
    
    knightsTour = KnightsTour()
    # print(knightsTour.find_knights_tour_bfs(5,5))
    # for experiment_num in range(1, 101):
    #     assert knightsTour.find_knights_tour_bfs(5,5) == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], "failed experiment" + str(experiment_num) + "in 5x5 chessboard experiments"

    # print(knightsTour.find_knights_tour_bfs(8,8))
    # for experiment_num in range(1, 101):
    #     assert knightsTour.find_knights_tour_bfs(8,8) == [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], "failed experiment" + str(experiment_num) + "in 8x8 chessboard experiments"

    # # print(knightsTour.find_knights_tour_bfs(17,11))    

    # print(knightsTour.find_knights_tour_dfs_iterative(5,5))
    # for experiment_num in range(1, 101):
    #     assert knightsTour.find_knights_tour_dfs_iterative(5,5) == [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], "failed experiment" + str(experiment_num) + "in 5x5 chessboard experiments"
    
    # print(knightsTour.find_knights_tour_dfs_iterative(8,8))
    # for experiment_num in range(1, 101):
    #     assert knightsTour.find_knights_tour_dfs_iterative(8,8) == [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], "failed experiment" + str(experiment_num) + "in 8x8 chessboard experiments"
    
    curr_position = (random.randint(0,5 - 1), random.randint(0,5 - 1))
    visited = set()
    chessboard = [[0 for x in range(5)] for y in range(5)]

    print(knightsTour.find_knights_tour_dfs_recursive(curr_position, chessboard, visited, 5,5))