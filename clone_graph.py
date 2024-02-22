from typing import Optional

class CloneGraph:

# """
# Definition for a Node.
    class Node:
        def __init__(self, val = 0, neighbors = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Depth first search recursive
        map = {}
        if node:
          cloneRoot = Node(node.val, None)
          map[node] = cloneRoot
          if node.neighbors:
              for neighbor in node.neighbors:
                  if neighbor in map:
                      cloneRoot.neighbors.append(map[neighbor])
                  else
                      cloneRoot.neighbors.append(cloneGraph(neighbor))
        return cloneRoot


if __name__== '__main__':    