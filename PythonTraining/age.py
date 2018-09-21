# Goal - print sum of years add upto current age!
# also show the age in months, days and hours

age = int(input("Enter your age :"))
i = 1;
cumage=0
while (i <= age):
    cumage = cumage+i
    i=i+1

print("Total Age in Years - ",cumage)
print("Total Age in Months - ",cumage*12)
print("Total Age in Days - ",cumage*12*365)
print("Total Age in Hours - ",cumage*12*365*24)
