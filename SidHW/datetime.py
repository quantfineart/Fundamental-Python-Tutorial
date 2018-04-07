import time
print("-----------------------------------------------------------------------------------------------------------------")
intup = str(input('Type "Confirm" to view the date and time.\n-----------------------------------------------------------------------------------------------------------------\n'))
print("-----------------------------------------------------------------------------------------------------------------")

if intup == "Confirm":
    print (time.strftime("The date is: %d/%m/%Y"))
    print (time.strftime("The time is: %H:%M"))
elif intup == "confirm":
    print(time.strftime("The date is: %d/%m/%Y"))
    print(time.strftime("The time is: %H:%M"))
else:
    print ("Confirmation not received.")
print("-----------------------------------------------------------------------------------------------------------------")
