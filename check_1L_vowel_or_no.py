text = input("Enter a string: ")
first_char = text[0].lower()   
if first_char in ['a', 'e', 'i', 'o', 'u']:
    print("The first letter is a vowel.")
else:
    print("The first letter is not a vowel.")