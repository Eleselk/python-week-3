temp = int(input("enter your temperature "))
a = input("for celcius type c, for fahrenheit type f")
if a == c:
    print("your temperature is ", (temp - 32) * 5/9)
else:
    print(temp * 9/5 + 32)