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
     
    

if __name__ == '__main__':
    pass