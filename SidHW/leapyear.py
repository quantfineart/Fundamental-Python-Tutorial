print("WELCOME TO SID'S LEAP YEAR CHECKER!")
print("-----------------------------------------")
Uyear = int(input("What is the year you would like to check?\n"))
a = 1

# NOTE For Kapil From Sid: Complicated Version (Activated)
if a == 1:
    if Uyear % 4 == 0:
        if Uyear % 100 == 0:
            if Uyear % 400 == 0:
                print("-----------------------------------------")
                print(Uyear, "is a leap year!")
                print("-----------------------------------------")
            else:
                print("-----------------------------------------")
                print(Uyear, "is not a leap year!")
                print("-----------------------------------------")
        else:
            print("-----------------------------------------")
            print(Uyear, "is a leap year!")
            print("-----------------------------------------")
    else:
        print("-----------------------------------------")
        print(Uyear, "is not a leap year!")
        print("-----------------------------------------")

# NOTE For Kapil From Sid: Simple Version (Deactivated)
if a == 0:
    if Uyear % 4 == 0:
        print("-----------------------------------------")
        print(Uyear, "is a leap year!")
        print("-----------------------------------------")
    else:
        print("-----------------------------------------")
        print(Uyear, "is not a leap year!")
        print("-----------------------------------------")