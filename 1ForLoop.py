alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = int(input("Enter size: "))
for i in range(1, size+1):
    print(" "*(size-i) + alpha[:i])
