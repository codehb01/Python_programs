# Print the grades of students after accepting the marks for 5 subjects from the user
s1 = int(input("Enter mark's of subject 1: "))
s2 = int(input("Enter mark's of subject 2: "))
s3 = int(input("Enter mark's of subject 3: "))
s4 = int(input("Enter mark's of subject 4: "))
s5 = int(input("Enter mark's of subject 5: "))

total = s1 + s2 + s3 + s4 + s5
average = total / 5 
percentage = (total / 500) * 100

print("Total marks: ", total)
print("Average marks: ", average)
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 50:
    print("Grade: E")
elif percentage >= 40:
    print("Grade: F")
else:
    print("Grade: Fail")
print("Percentage: ", percentage, "%")