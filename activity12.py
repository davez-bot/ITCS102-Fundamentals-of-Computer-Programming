name = input("Please input your name --->")

age = int(input("Please input your age --->"))

if age  >= 0 and age <= 5:
    print("That age is considered as INFANT")
elif age >= 6 and age <= 12:
    print("That age is considered as KID")
elif age >= 13 and age <= 15:
    print("That age is considered as PRE-TEEN")
elif age >= 16 and age <= 19:
    print("That age is considered as TEENAGER")
elif age >= 20 and age <= 29:
    print("That age is considered as EARLY ADULTHOOD")
elif age >= 59 and age <= 60+:
    print("That age is considered as SENIOR CITIZEN")
else:
     print("You are 6-foot underground")
