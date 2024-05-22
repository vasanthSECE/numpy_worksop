#write a program to find the sum of digits of a given number'
def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n = n // 10
    return sum_digits
number = 12345
print("Sum of digits:", sum_of_digits(number))  
