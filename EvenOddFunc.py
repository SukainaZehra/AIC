#Question: Takes an input from user and return whether its odd or even

a1 = int(input("Enter no: "))
def evenOdd(n1):
    if(n1%2==0):
        return("Even")
    else:
        return("Odd")

res = evenOdd(a1)
print("Result= ",res)