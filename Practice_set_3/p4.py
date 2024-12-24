# write a python program to sum a list with 4 numbers.
num = []
for i in range (4):
  m = int(input("Enter a number for sum ::"))
  num.append(m)
  i+=1

print("Your Entered number is ::")
print(num)
print("Sum of these number is ::",sum(num))