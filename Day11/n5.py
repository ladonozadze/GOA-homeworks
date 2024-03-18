sum=0
num=1
n=int(input("enter positive numbers: "))

while num>=0:
    num=int(input("enter one more: "))
    if num<0:
        print(".")
    

    sum=sum+num
print(sum+n)
    