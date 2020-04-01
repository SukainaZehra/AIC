#checking whether a number is completely divisible by another number
num1 = int(input("Enter a number: "))
num2 = int(input("Enter aother number: "))
if num1>num2 and num2>0 :
   if num1%num2 == 0 :
    print(num1, " is completely divisible by ", num2)
   else:
    print(num1, " is not completely divisible by ", num2)
else:
    print("INVALID INPUTS!!!!! \n please make sure that num1 should be greater than num2 and num2 should greater than ZERO")