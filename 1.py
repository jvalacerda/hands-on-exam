a = int(input("Write a position for the Fibonacci sequence:"))

b = 1
c = 0
 
if a <= 0: # Checks if the position is negative or zero
    print("Error! Value is negative.")
elif a == 1: # Prints if the position is 1
    print(a)
else:
    print(1)
    for i in range(1, a): # Calculates the sum of the number with its previous position
        d = b + c
        c = b
        b = d
        print(b)
    