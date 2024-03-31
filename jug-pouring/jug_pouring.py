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
    

     
    

if __name__ == '__main__':
    pass