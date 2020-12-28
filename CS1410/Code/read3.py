# Illustrates str.readlines

with open("fib.py") as f:
	lines = f.readlines()

for line in lines:
	print(line,end='')