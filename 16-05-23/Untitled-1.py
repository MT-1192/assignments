t = float(input("Enter temperature in celsius: "));
if t < -273.15:
    print("Temperature is invalid");
elif t  == -273.15 <= t < 0:
    print("Temperature is below freezing");
elif 0 < t < 100:
    print("Temperature is in the normal range");
else:
    print("Temperature is above the boiling point");