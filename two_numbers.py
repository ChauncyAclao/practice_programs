
numbers = []


for n in range(2):
        while True:
                try:
                        num = int(input("number: "))

                        numbers.append(int(num))
                       
                        break
                        
                
                except ValueError:
                        print('try again')

print(numbers)

highest_number = max( number for number in numbers)
lowest_number = min(number for number in numbers)
sum = sum(number for number in numbers)
diff = numbers[0] - numbers[1]
product = numbers[0] * numbers[1]
quotient = numbers[0] / numbers[1]
remainder = numbers[0] % numbers[1]
raised = numbers[0] ** numbers[1]

if highest_number != lowest_number:
        print("not equal")
        print("high number:",highest_number)
        print("lownumber:",lowest_number)
else:
        print("equal")

print("sum:", sum)
print("diff:", diff)
print("product:", product)
print("quotient w/o decimal:", int(quotient))
print("quotient rounded up:", round(quotient))
print('quotient:', quotient)
print("remainder:", remainder)
print("first number raised to the secod number:", raised)

