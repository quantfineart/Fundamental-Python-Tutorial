userinput = input("Please enter your string.\n----------------------------------------------------------------------------------------------------------------------\n")
print("----------------------------------------------------------------------------------------------------------------------")

swap = {'.':',',',':'.'}
def switch(x):
    x = ''.join(swap.get(k, k) for k in x)
    print (x)


z = switch(userinput)
print("Your string backwards is:", z)
print("----------------------------------------------------------------------------------------------------------------------")

