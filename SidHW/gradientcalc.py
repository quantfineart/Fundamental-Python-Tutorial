m = 0
print("WELCOME TO SID'S GRADIENT CALCULATOR!")
print("--------------------------------------------------")

c = float(input("What is the constant term of the line? (c)\n"))
print("--------------------------------------------------")

x = float(input("Ok, now what is the x-value? (x)\n"))
print("--------------------------------------------------")

y = float(input("Ok, now what is the y-value? (y)\n"))
print("--------------------------------------------------")

m = (y - c)/x

print("Alright! The gradient of your line is: {}".format(m))
print("--------------------------------------------------")
print("Also, the equation of your line is: y = {}x + {}".format(m, c))
print("--------------------------------------------------")




