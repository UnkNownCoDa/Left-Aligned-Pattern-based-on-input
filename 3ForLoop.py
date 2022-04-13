size = int(input("Enter size: "))
for i in range(0, size):
  ch = 65
  for j in range(0, size-1):
    print(" ", end="")
  for k in range(0, i+1):
    print(chr(ch+k), end="")
  print()
