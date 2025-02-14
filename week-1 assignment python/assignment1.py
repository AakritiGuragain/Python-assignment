#Qno.1
decimal = float(input("Enter a decimal number: "))
#asking the user
integer = int(decimal)
string = (decimal)
print(f"Float:{decimal}")
print(f"Integer value:{integer}")
print(f"String value:{string}")

#Qno.2
Name = input("Enter your name: ")
print(f"{Name[0].upper()} {Name.split()[-1][0].upper()}")

#Qno.3
Text = input("Enter your text to reverse: ")
print(f"{Text[::-1]}")

#Qno.4
Word = input("Enter here word: ")
index = int (input("Enter index you want: "))
print(f"{Word[index:]}")

#Qno.5
Email = input("Enter your email adress: ") 
print(f"{Email.split('@')[-1]}")

#Qno.6
Give = input("Enter:")
print(f"{Give[-1]+Give[1:-1]+Give[0]}")