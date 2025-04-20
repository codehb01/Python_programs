# Program 10: Display count of vowels, consonants, blank spaces, special symbols and digits in a given STRING.

myString = "John Doe is 2nd *Data Scientist* in a MNC from our campus"
countVow = 0
countInt = 0
countCons = 0
countSp = 0
countSpace = 0
vowels = ['a','e','i','o','u']
specialSymbols = ['!','@','#','$','%','^','*']

for i in myString:
    if i.lower() in vowels:
        countVow += 1
    elif i in specialSymbols:
        countSp += 1
    elif i.isdigit():
        countInt += 1
    elif i == ' ':
        countSpace += 1
    elif i.isalpha():
        countCons += 1

print("Number of Integers      :", countInt)
print("Number of Vowels        :", countVow)
print("Number of Consonants    :", countCons)
print("Number of Special Chars :", countSp)
print("Number of Spaces        :", countSpace)