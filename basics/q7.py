#Sum of digits
def sum_of_digits(n):
    return sum(int(i) for i in str(n))
a=int(input("enter a number:"))
print(sum_of_digits(a))
