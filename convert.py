def celsiusToFahrenheit(celsiusTemperature):
    fahrenheit = celsiusTemperature * (9.0/5.0) + 32.0
    return fahrenheit

def fahrenheitToCelsius (fahrenheitTemperature):
    celsius = (fahrenheitTemperature - 32.0) * (5.0/9.0)
    return celsius

def showMenu():
    print ("A: Convert celsius to fahrenheit")
    print ("B: Convert fahrenheit to celsius")
    print ("X: Exit")

showMenu()
option = input("Option")

while option != "X":
    if option =="A" or option =="B":
        value = input("Number to convert:")
        if option =="A":
            print (celsiusToFahrenheit (float(value)))
        elif option =="B":
            print (fahrenheitToCelsius (float(value)))
    else:
        print ("Please enter a valid option")

    showMenu()
    option = input("Option:")
    
