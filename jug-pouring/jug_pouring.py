class JugPouring:
    #Jug Pouring Problem:
    # Given a 3 gallon jug and a 5 gallon jug, can you measure exactly 4 gallons of water?
    #Abstract away this problem into a graph and see how you can apply graph search to solve this problem
    #starting state --> different combinations of operations/paths you can take to reach --> goal state
    #different operations --> pour 3 gallons into 3 gallon jug , pour 5 gallons into 5 gallon jug
    #pour 3 gallons out of 3 gallon jug, pour 5 gallons out of 5 gallon jug, transfer from 5 gallon to 3 gallon, transfer from 3 to 5 gallon
    # empty 3 gallon --> fill 3 gallon jug  --> fill                       4 gallons
    # and 5 gallon jugs-->      -->
    #An idea could be to find the shortest path from initial node (empty 3 gallon and 5 gallon jugs) to goal node (4 gallons)
    #Use list to represent how much to represent how much the 3 gallon and 5 gallon jugs are filled [a,b]
    #for ex. [1, 3] means the 3 gallon jug has 1 gallon and 5 gallon jug has 3 gallons

    #Model jug pouring problem as a set of finite states (a,b) representing how many gallons are in 3 and 5 gallon jugs respectively
    #Starting state: (0, 0)
    #Goal state: (x, 4)
    #State transitions: 
    #empty 3: (a,b) -> (0, b)
    #empty 5: (a,b) -> (a, 0)
    #fill 3: (a,b) -> (3,b) 
    #fill 5: (a,b) -> (a, 5)   
    #transfer from 3 to 5: (a,b) -> (max(0, a-(5 - b)), min (a + b, 5))
    #transfer from 5 to 3: (a,b) -> (min(3, a+b ), max(b-(3-a), 0))

    #We can build graph/path as we go instead of building entire graph first and then searching
    # TODO: try to figure approach where you build a graph/path as you go to solve this problem
    #Approach 1:
    #JugState
    #three_gallon=''
    #five_gallon=''
    #neighbors = []
    #state_transitions = ['empty 3', 'empty 5', 'fill 3', 'fill 5', 'transfer from 3 to 5', 'transfer from 5 to 3']
    #Start with start_state = JugState(0, 0, None)
    #bfsQ = []
    #bfsQ.append(start_state)
    #depth = 0
    #while bfsQ:
    #   curr_state = bfsQ.pop()
        #for transition in state_transitions:
        #   next_state = JugState(0, 0, None)
        #   if transition == 'empty 3':
        #       next_state.three_gallon = 0
        #   elif transition == 'empty 5':
        #       next_state.five_gallon = 0
        #   elif transition == 'fill 3':
        #       next_state.three_gallon = 3
        #   elif transition == 'fill 5':
        #       next_state.five_gallon = 5
        #   elif transition == 'transfer from 3 to 5':
        #       if next_state.three_gallon < (5 - next_state.five_gallon):
        #           next_state.five_gallon += next_state.three_gallon
        #           next_state.three_gallon = 0
        #       else:        
        #           next_state.five_gallon = 5
        #           next_state.three_gallon -= (5-jug_state.five_gallon)
        #   elif transition == 'transfer from 5 to 3':
        #       if next_state.five_gallon >= (3 - next_state.three_gallon):
        #           next_state.five_gallon -= (3 - next_state.three_gallon)
        #           next_state.three_gallon = 3
        #       else:        
        #           next_state.five_gallon = 0
        #           next_state.three_gallon += next_state.five_gallon
        #   if next_state.five_gallon == 4
        #       return depth
        #   bfsQ.append(next_state)
        #depth += 1
        #time: O(d) where d = depth to reach five_gallon == 4
        #space: O()
    class JugState:

        def __init__(self, three_gallon, five_gallon):
            self.three_gallon = three_gallon
            self.five_gallon = five_gallon
     
    def get_smallest_steps_to_solve_jug_pouring_problem(self):
        state_transitions = ['empty 3', 'empty 5', 'fill 3', 'fill 5', 'transfer from 3 to 5', 'transfer from 5 to 3']
        start_state = self.JugState(0, 0)
        bfsQ = []
        bfsQ.append(start_state)
        depth = 0
        visited = []
        while bfsQ:
            curr_state = bfsQ.pop(0)
            curr_state_tuple = (curr_state.three_gallon, curr_state.five_gallon)
            if curr_state_tuple not in visited:
                visited.append(curr_state_tuple)
                print("three gallon has " + str(curr_state.three_gallon) + " and five gallon has " + str(curr_state.five_gallon) + " at the current state")
                for transition in state_transitions:
                    print('current transition is ' + transition)
                    next_state = self.JugState(curr_state.three_gallon, curr_state.five_gallon)
                    if transition == 'empty 3':
                        next_state.three_gallon = 0
                    elif transition == 'empty 5':
                        next_state.five_gallon = 0
                    elif transition == 'fill 3':
                        next_state.three_gallon = 3
                    elif transition == 'fill 5':
                        next_state.five_gallon = 5
                    elif transition == 'transfer from 3 to 5':
                        if next_state.three_gallon <= (5 - next_state.five_gallon):
                            next_state.five_gallon += next_state.three_gallon
                            next_state.three_gallon = 0
                        else:        
                            next_state.five_gallon = 4
                            next_state.three_gallon -= (4-next_state.five_gallon)
                    elif transition == 'transfer from 5 to 3':
                        if next_state.five_gallon >= (3 - next_state.three_gallon):
                            next_state.five_gallon -= (3 - next_state.three_gallon)
                            next_state.three_gallon = 3
                        else:        
                            next_state.five_gallon = 0
                            next_state.three_gallon += next_state.five_gallon
                    if next_state.five_gallon == 4:
                        return depth
                    print("three gallon of next state is " + str(next_state.three_gallon) + " and five gallon is " + str(next_state.five_gallon))
                    if next_state.three_gallon != 0 or next_state.five_gallon != 0:
                        bfsQ.append(next_state)
                depth += 1
                # print(bfsQ)
        return -1
    
if __name__ == '__main__':
    
    jugPouring = JugPouring()
    minimum_steps = jugPouring.get_smallest_steps_to_solve_jug_pouring_problem()
    print(minimum_steps)