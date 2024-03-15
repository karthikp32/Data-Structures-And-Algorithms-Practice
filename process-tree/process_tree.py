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
    pass
if __name__== '__main__': 
    pass