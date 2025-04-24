# Program 10: Display count of vowels, consonants, blank spaces, special symbols and digits in a given STRING.

# Program: Count vowels, consonants, spaces, special symbols, and digits in a string

vowels = "aeiouAEIOU"
digits = "0123456789"
special_symbols = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"

count_vowels = 0
count_consonants = 0
count_spaces = 0
count_special = 0
count_digits = 0

user_input = input("Enter a string: ")

for char in user_input:
    if char in vowels:
        count_vowels += 1
    elif char.isalpha():
        count_consonants += 1
    elif char in digits:
        count_digits += 1
    elif char == " ":
        count_spaces += 1
    elif char in special_symbols:
        count_special += 1

print("\nResults:")
print("Vowels:", count_vowels)
print("Consonants:", count_consonants)
print("Digits:", count_digits)
print("Blank spaces:", count_spaces)
print("Special symbols:", count_special)
