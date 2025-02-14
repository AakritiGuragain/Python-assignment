#qno.1
numbers = input("Enter the numbers seperating by space: ").split()
#taking input of list
numbers=[int(num)for num in numbers]
for num in numbers:
    if num>50:
        print("Number more than 50")
        break
    if num %5 == 0:
        continue
    print(num)

#qno.2

    
