class DepthFirstSearchAndBreadthFirstSearch:

    
    #Class of Problems Depth First Search is Useful for:
    #1) Find a leaf a quicker

    #Class of Problems Breadth First Search is Useful for:
    #1) Traverse nodes in a tree/graph level by level
    #   For ex. print out the nodes in a family tree, i.e. grandparents, parents, children
    #2) Find shortest path/minimum depth to a node with certain characteristic
    #   For ex. find the first person in the family with a name starting with "A" given 
    #       how much information about the family tree we have 

    def dfs_recursive(self, tree):
        root, children = tree
        print(root)
        for c in children:
            self.dfs_recursive(c)

    def dfs_iterative(self, tree):
        stack = [tree]
        while stack:
            node, children = stack.pop()
            print(node)
            for child in reversed(children):
                stack.append(child)

    #Stack
    #['E', []]
    #['D', []]


    #printed logs
    #A
    #C
    #G
    #F
    #B
    #E
    #D
    def bfs_iterative(self, tree):
        queue = [tree]
        while queue:
            node, children = queue.pop(0)
            print(node)
            for child in children:
                queue.append(child)

    #Queue

     #A
     #            


if __name__== '__main__':
    #tree node represented as [node, [list of child nodes]]
    tree = ['A', [['B', [['D', []], ['E', []]]], ['C', [['F', []], ['G', []]]]]]
    dfs_bfs = DepthFirstSearchAndBreadthFirstSearch()
    dfs_bfs.dfs_recursive(tree)
    print('\n')
    dfs_bfs.dfs_iterative(tree)
    print('\n')
    dfs_bfs.bfs_iterative(tree)