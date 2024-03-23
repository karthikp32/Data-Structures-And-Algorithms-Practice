import sys

class ProcessTree:
    #Problem Defintion: Create Process Tree of Running Processes from ps linux command output 
    #Ex. 1
    #Input:
    #PID    PPID    CMD
    # 1        0    bash
    # 2        1    ps -o pid,ppid,cmd
    # 3        1    sleep 120
    #Output: 
    #bash(1)--ps -o pid,ppid,cmd(2)
    #        |
    #        --sleep(3)

    #Ideas for implementation
    #Read output of ps command from standard input stream 
    #One way is to feed it in as input 
    #to the python script 
    #ps -o pid,ppid,cmd | python3 process_tree.py
    #can alias python3 process_tree.py as ptree
    #so I can execute ps -o pid,ppid,cmd | ptree

    #Approach 1:
    #Read in each line of ps -o pid,ppid,cmd output and Build Process Tree
    #parse out process id, parent process id, and command
    #and store in one ProcessTreeNode
    #set root node equal to first node
    #use dictionary to store pid:cmd
    #use dictionary to store alreadyCreatedNodes pid:ProcessTreeNode(pid)
    #ProcessTreeNode(val)
    #   self.node = ''
    #   self.children = []
    #set processTreeNode.node = ppid
    #if pid in alreadyCreatedNodes
    #processTreeNode.children.append(alreadyCreatedNodes[pid])
    #else
    #processTreeNode.children.append(ProcessTreeNode(pid))

    #if current node's PID equals PPID of root node
    #set rootNode equal to that node
    #parent pointer or child pointer or both?

    #traverse from root node to child nodes, grandchildren nodes, etc.
    #in breadth first search fashion
    #construct pstree visual as traverse each node
    #if you are accessing root node
    #add root node's command to visual
    #if you are accessing first child node
    #add "-" + first child node's command to visual
    #if you are accessing second+ child node
    #add "|\n-" +  second+ child node's command to visual
    #time: O(n)
    #space: O(n)


    class ProcessTreeNode:

         def __init__(self, val, children):
            self.val = val
            self.children = children


    def parse_pid_ppid_cmd_from_line(self, line):
        active_processes_info = line.split()
        pid = active_processes_info[0]
        ppid = active_processes_info[1]
        cmd = active_processes_info[2]
        return pid, ppid, cmd

    def parse_out_process_tree_nodes(self, pid_cmd_pairs, already_created_nodes, root):
        for line in sys.stdin:
            pid, ppid, cmd = self.parse_pid_ppid_cmd_from_line(line)
            pid_cmd_pairs[pid] = cmd
            if pid not in already_created_nodes:
                already_created_nodes[pid] = self.ProcessTreeNode(pid, [])
            if ppid in already_created_nodes:
                already_created_nodes[ppid].children.append(pid)
                root = already_created_nodes[ppid]
        print(root.val)        
        return root        

    def traverse_and_build_process_tree_visual(self, root_node):
        pass

    def print_process_tree_visual(self, process_tree_visual):
        pass

    pass
if __name__== '__main__': 

    processTree = ProcessTree()
    
    pid_cmd_pairs = {}
    already_created_nodes = {}
    root = None
    processTree.parse_out_process_tree_nodes(pid_cmd_pairs, already_created_nodes, root)
        
        