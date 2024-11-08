
while True:
    try: 
        num1 = int(input("first number:"))
        num2 = int(input("second number:"))
       
        numbers_between = []

        break

    except ValueError:
        print("try again")

if num1 > num2 :
    num1,num2 = num2, num1 

    for i in range(num1 + 1, num2):
        numbers_between.append(i)

    if numbers_between:
        print(numbers_between)

    else:
        print("no value")

else:
    for i in range(num1 + 1, num2):
        numbers_between.append(i)

    if numbers_between:
        print(numbers_between)

    else:
        print("no value")
    
    



    
