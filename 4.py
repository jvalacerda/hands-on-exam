n = int(input("Enter the size of the array: "))

numbers = [n]

for i in range(0, n):
    numbers.append(input("Enter a number: "))

numbers.sort(reverse = True)

for i in range(0, n):
    print(numbers[i])