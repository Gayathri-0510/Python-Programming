def character(x):
    if x.isalpha():
        print(x, " is a character")
    else:
        print(x, " is not a character")
s=str(input("Enter input : "))
character(s)