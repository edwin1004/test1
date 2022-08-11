Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Amount = int(input("Enter the amount:"))
Enter the amount: 100
>>> print("Quarters =", Amount // 25)
Quarters = 3
>>> Amount = Amount % 25
>>> print("Dimes =", Amount // 10)
Dimes = 1
>>> Amount = Amount % 10
>>> print("Nickels =", Amount // 5)
Nickels = 1
>>> Amount = Amount % 5
>>> print("Cents =", Amount // 1)
Cents = 3
>>> print ("My name is Chan Chun Hei Edwin, and the SID is 55694360")
My name is Chan Chun Hei Edwin, and the SID is 55694360
>>> Amount = int(input("Enter the amount:"))
Enter the amount: 99
>>> print("Quarters =", Amount // 25)
Quarters = 3
>>> Amount = Amount % 25
>>> print("Dimes =", Amount // 10)
Dimes = 2
>>> Amount = Amount % 10
>>> print("Nickels =", Amount // 5)
Nickels = 0
>>> Amount = Amount % 5
>>> print("Cents =", Amount // 1)
Cents = 4
>>> 
