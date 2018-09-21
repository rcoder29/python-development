name = input("Enter your name :")
age = int(input("Enter your age : "))

print("Your Name : ", name)
print("Your Age :", age)
print ("Your Name and Age : ", name, age)

combinedvar = name+str(age)
print("Your Name and Age as one variable :", combinedvar)

# print a character in a string
print("Last character of Name : ", name[len(name)-1])

# print character by charter with a seperator
for c in name:
    print(c,":")
