# Program 17 : Write a program to implement multiple exceptions handling such as ValueError, KeyError, PermissionError, General exception within a standard LOGIN process (Login successful, User doesn’t exist, Incorrect password, Too many attempts, etc.).

users = {
    "Max": "Formula1",
    "Cristiano": "Siuu",
    "admin": "admin@123"
}

maxAttempts = 3
attempts = 0

while attempts < maxAttempts:
    try:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            raise ValueError("Empty fields input not provided.")

        if username not in users:
            raise KeyError("User doesn't exist.")

        if users[username] != password:
            raise PermissionError("Incorrect password!")

        print("Login successful! Welcome", username)
        break

    except ValueError as ve:
        print("ValueError:", ve)

    except KeyError as ke:
        print("KeyError:", ke)

    except PermissionError as pe:
        print("PermissionError:", pe)

    except Exception as e:
        print("An unexpected error occurred:", e)

    attempts += 1
    print("Attempts left:", maxAttempts - attempts)

if attempts == maxAttempts:
    print("Too many login attempts! Try again later.")

    