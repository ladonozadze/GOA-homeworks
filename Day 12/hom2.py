choice=input("choose , Kilometers to miles or miles to kilometers :")

if choice=="kilometers to miles":
    num=int(input("enter the number :"))
    print( num / 1.609344)

if choice=="miles to kilometers":
    num1=int(input("enter the number :"))
    print( num1 * 1.609344)

else:
    print("wrong decision!")
    