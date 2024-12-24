# write a python program to accept marks of 5 students and display them in a sorted manner.
mark = []
for i in range (5):
  m = int(input(f"Enter a mark of student {i+1} ::"))
  mark.append(m)
  i+=1

print(mark)
mark.sort()
print("Mark in sorted manner ::")
print(mark)