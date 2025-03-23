num = int(input("Enter number for table:"))
result = {}  # Initialize result as a dictionary
for tab in range(1, 10+1):
    if tab==5:
        continue
    result[tab] = num * tab  # Store the result for each multiplication
    output = "{} * {} = {}"
    print(output.format(num, tab, result[tab]))  # Access the correct value from the dictionary