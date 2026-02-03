#Even/odd check
def e_o(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
    
a=int(input("Enter a number:"))
print(e_o(a))