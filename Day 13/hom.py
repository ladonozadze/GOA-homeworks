age=int(input("enter your age :"))
if age<18:
    print("You are a minor")
elif age in range(18,65):
    print("You are an adult.")  
else:
    print("You are a senior citizen")      