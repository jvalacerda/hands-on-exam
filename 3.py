n = int(input("Enter a number: "))

if n <= 1: # Checks if the position is negative, zero or 1
    print("Number should be greater than 1")
elif n > 1:
    for i in range(2, n + 1): # Search for a number that is devided by n
        if (n % i) == 0:
            print("Prime Number")
            break
        else:
            print("Not a Prime Number")
