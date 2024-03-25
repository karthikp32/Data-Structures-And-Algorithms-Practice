sleep 1000 &
ps -o pid,ppid,cmd | python3 process_tree.py
