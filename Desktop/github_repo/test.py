def suma(a, b):
    if a.isnumeric() == True and b.isnumeric() == True:
        return(int(a) + int(b))
    else:
        return("Unhandled exception [btw it's not unhandled cuz you cannot add letters XD ']")

print("Enter numbers")
a = input("First number : ")
b = input("Second number : ")
print(suma(a, b))
