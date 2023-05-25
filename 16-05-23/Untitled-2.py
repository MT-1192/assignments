'''age = int(input("Enter the age: "));
if age < 18:
    print("The user is not old enough to vote");
elif age == 18 and age < 65:
    print("The user is eligible to vote");
elif age > 65:
    print("The user is eligible to vote,but they may choose to retire instead.");
    '''


password = input("Please enter the password: ");
if len(password) < 8:
    print("Try again");
elif len(password) == 8 and len(password) <= 12:
    print("The password is medium strength");
elif len(password) > 12:
    print("The password is strong.");



