phrase = input("Enter a phrase: ")

phrase_without_spaces = phrase.replace(' ', '')

if(phrase_without_spaces == phrase_without_spaces[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")