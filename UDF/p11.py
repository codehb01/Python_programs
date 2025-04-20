# Program 11 : Calculate library fine based on 2 conditions, a) Book return date and b) Book condition
from datetime import datetime

def calculate_fine(due_date_str, return_date_str, condition):
    # Convert string dates to datetime objects
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    
    fine = 0
    
    # Check for late return
    if return_date > due_date:
        late_days = (return_date - due_date).days
        fine += late_days * 5  # ₹5 per late day
    
    # Check for damaged book
    if condition.lower() == "damaged":
        fine += 100  # ₹100 fine
    
    return fine

# Input
due_date_input = input("Enter Due Date (YYYY-MM-DD): ")
return_date_input = input("Enter Return Date (YYYY-MM-DD): ")
book_condition = input("Enter Book Condition (Good/Damaged): ")

# Calculate fine
total_fine = calculate_fine(due_date_input, return_date_input, book_condition)
print(f"\nTotal Library Fine: ₹{total_fine}")
