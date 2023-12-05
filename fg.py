Задание 1:
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

even_sum = 0
odd_sum = 0
multiple_9_sum = 0
even_count = 0
odd_count = 0
multiple_9_count = 0

for i in range(num1, num2+1):
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_sum += i
        odd_count += 1
    if i % 9 == 0:
        multiple_9_sum += i
        multiple_9_count += 1

print("Сумма четных чисел:", even_sum)
print("Среднее арифметическое четных чисел:", even_sum/even_count)
print("Сумма нечетных чисел:", odd_sum)
print("Среднее арифметическое нечетных чисел:", odd_sum/odd_count)
print("Сумма чисел, кратных 9:", multiple_9_sum)
print("Среднее арифметическое чисел, кратных 9:", multiple_9_sum/multiple_9_count)

Задание 2:
length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")

for i in range(length):
    print(symbol)




    3




    
    
while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")





        4



sum = 0
max_num = float('-inf')
min_num = float('inf')

while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    else:
        sum += num
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

print("Сумма введенных чисел:", sum)
print("Максимальное число:", max_num)
print("Минимальное число:", min_num)
