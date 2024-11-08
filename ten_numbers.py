
numbers = []

for i in range(10):
    while True:
        try:
            num = int(input("number:"))

            numbers.append(num)

            break
        except ValueError:
            print("try again")

print(numbers)

sum = sum(number for number in numbers)
difference  = numbers[0] - numbers[1] - numbers[2] - numbers[3] - numbers[4] - numbers[5] - numbers[6] - numbers[7] - numbers[8] - numbers[9]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print("total:", sum)
print("differece:", difference)
print("even numbers:", even_numbers)
print("how many even:", len(even_numbers))
print("even numbers:", odd_numbers)
print("how many even:", len(odd_numbers))
