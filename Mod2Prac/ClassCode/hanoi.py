''' hanoi.py: Solves the Towers of Hanoi problem recursively '''
def move(n, source, dest, temp):
   if (n > 1):
      move(n-1, source, temp, dest);
      move(1, source, dest, temp);
      move(n-1, temp, dest, source);
   else:
      print("Move from",source,"to",dest)

def hanoi(n):
   assert n > 0
   print("Moving",n,"disks:")
   move(n, "Peg-1", "Peg-3", "Peg-2")

for n in range(1,4):
   hanoi(n)
   print()

''' Output:
Moving 1 disks:
Move from Peg-1 to Peg-3

Moving 2 disks:
Move from Peg-1 to Peg-2
Move from Peg-1 to Peg-3
Move from Peg-2 to Peg-3

Moving 3 disks:
Move from Peg-1 to Peg-3
Move from Peg-1 to Peg-2
Move from Peg-3 to Peg-2
Move from Peg-1 to Peg-3
Move from Peg-2 to Peg-1
Move from Peg-2 to Peg-3
Move from Peg-1 to Peg-3
'''
