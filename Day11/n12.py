number1=int(input("enter a number: "))

while number1!=(number1%2==0):
    number1=int(input("try again: "))
    if number1%2==0:
        print("correct, this number is even")
    
