string = str(input("enter a filename"))

a = string.find(".")
extension = string[a+1:]
print(extension)