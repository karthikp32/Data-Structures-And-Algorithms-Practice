sleep 20 &
ps --sort -pid -o pid,ppid,cmd | python3 process_tree.py
