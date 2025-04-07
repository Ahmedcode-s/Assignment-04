print("Welcome to Fahrenheit to Celsius convertor app")

#fahrenheit temp given by the user
fahren_temp = float(input("Please the enter the fahrenheit temperature: "))

#Formula to convert fahrenheit in celsius
Cel_temp = (fahren_temp - 32)*5.0/9.0

#final result!
print(f"The Fahrenheit temperature {fahren_temp} is {Cel_temp} in Celsius.") 