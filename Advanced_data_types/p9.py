# Program 9 : Demonstrate LIST comprehensions using two examples.
# Example 1: Creating a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("List of squares from 1 to 10:", squares)
# Example 2: Creating a list of even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("List of even numbers from 1 to 20:", even_numbers)