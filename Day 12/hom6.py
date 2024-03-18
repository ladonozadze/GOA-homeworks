num1=int(input("enter the number :" ))
num2=int(input("enter the number2 :"))

if num1>num2:
    for i in range(num2,num1):
        print(i**3)
elif num2>num1:
    for i in range(num1,num2):
        print(i**3)
