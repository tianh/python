age=11
guess_age=int(input(">>:"))
if guess_age==age:
    print("yes")
elif guess_age>age:
    print("try smaller")
elif guess_age<age:
    print("try bigger")

else:
    print("no")
