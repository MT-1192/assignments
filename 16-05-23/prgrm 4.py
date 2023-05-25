sub1 = int(input("enter sub1 marks: "))
sub2 = int(input("enter sub2 marks: "))
sub3 = int(input("enter sub3 marks: "))
sub4 = int(input("enter sub4 marks: "))
total = (sub1 + sub2 + sub3 + sub4)
average = total/4
if average >= 90 and average <= 100:
    print("Your grade is A")
elif average >= 70 and average <= 90:
    print("Your grade is B")
elif average >= 50 and average <= 70:
    print("Your grade is C")
elif average >= 30 and average <= 50:
    print("Your grade is D")
else:
    print("Given input is Invalid.")