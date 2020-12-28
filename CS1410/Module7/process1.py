''' process1.py:

    Shows how to launch processes, sending and receiving data.
    Launches a native executable (trinum) and shell commands.

Output:
======
1 
1 3 6 10 15 
1 3 6 10 15 
Output of trinum 10: 1 3 6 10 15 21 28 36 45 55 

-rw-r--r--@ 1 chuck1  staff  299 Sep  3 17:42 fib.py
-rw-r--r--@ 1 chuck1  staff  303 Sep  2 17:58 fib2.py
-rw-r--r--@ 1 chuck1  staff  434 Sep  5 14:37 fib2_perf.py
-rw-r--r--@ 1 chuck1  staff  126 Sep  2 17:56 fib3.py
-rw-r--r--@ 1 chuck1  staff  250 Sep  5 14:37 fib3_perf.py
-rw-r--r--@ 1 chuck1  staff  382 Sep  5 14:37 fib_perf.py
-rw-r--r--  1 chuck1  staff  507 Sep 26 15:55 filedialog.py
-rw-r--r--  1 chuck1  staff  494 Sep 12 20:37 filter_impl.py
-rw-r--r--  1 chuck1  staff  141 Aug 29 15:25 fraction.py

3:-rw-r--r--@ 1 chuck1  staff  434 Sep  5 14:37 fib2_perf.py
5:-rw-r--r--@ 1 chuck1  staff  250 Sep  5 14:37 fib3_perf.py
6:-rw-r--r--@ 1 chuck1  staff  382 Sep  5 14:37 fib_perf.py

4:bunch
7:on
9:own
10:line
'''

import subprocess

# Run a native executable program
subprocess.run('./trinum')

# Calling a native executable program with a command-line argument, Method 1
subprocess.run(['./trinum','5'])

# Calling a native executable program with a command-line argument, Method 2 (via a shell; slower)
subprocess.run('./trinum 5',shell=True)

# Capturing the output locally
proc = subprocess.run(['./trinum','10'],capture_output=True,text=True)
print('Output of trinum 10:',proc.stdout)

# Get a directory listing of files starting with 'f'
proc = subprocess.run('ls -l f*',shell=True,capture_output=True,text=True)
print(proc.stdout)

# Send output of one process into another
proc1 = subprocess.run('ls -l f*',shell=True,capture_output=True,text=True)
proc2 = subprocess.run('grep -n perf',shell=True,input=proc1.stdout,capture_output=True,text=True)
print(proc2.stdout)

# Send local data into a subprocess
data = 'this\nis\na\nbunch\nof\nwords\non\ntheir\nown\nline'
subprocess.run('grep -n n',shell=True,text=True,input=data)
