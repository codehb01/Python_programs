movieN=int(input("---Welcome to PVR---\nMovies Screening\n1.Chaava\n2.Captain America\n3.Brutalist\n4.Avengers\nPlease enter movie number: "))
Day=int(input("\nPlease select your day\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n"))
age=int(input("Please enter your age: "))

if Day==3:
    if age<18:
            print("You've got discount of $2.\nPay only $6.00")
    else:
          print("You've got discount of $2.\nPay only $10.00")
else:
      if age<18:
            print("Pay $8 and book your ticket!")
      else:
            print("Pay $12 and book your ticket!")

