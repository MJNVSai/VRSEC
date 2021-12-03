p = input("enter a character or digit: ")

if p.islower():
    print(" it is a lower case character ")
elif p.isupper():
    print(" it is a upper case character ")
elif p.isdigit():
    print(" it is a digit ")
else:
    print(" input error ")
