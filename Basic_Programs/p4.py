# Program 4 : Display, i) a pattern formed with numbers and, ii) a pattern formed with ‘*’ using nested looping.

# i) Pattern with numbers
print("Pattern with numbers:")
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

# ii) Pattern with '*'
print("\nPattern with '*':")
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()