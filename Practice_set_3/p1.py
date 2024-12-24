# write a python program to store 4 fruits name in a list entered by the user
fruits = []

for i in range (4):
  f1 = input(f"Enter a {i+1} fruit name ::")
  fruits.append(f1)
  i+=1

print(fruits)