"""
This Python Script will convert values between 3 units which is Celsius, Fahrenheit, and Kelvin.
This tool works by choosing a conversion setting from the list and then writing the values to convert them.
wrote by Khaled Alshamsi
"""
print("""

 /$$$$$$$$ /$$                                                                                    /$$                        
|__  $$__/| $$                                                                                   | $$                        
   | $$   | $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$    /$$  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
   | $$   | $$__  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$|  $$  /$$/ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
   | $$   | $$  \ $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$  \ $$ \  $$/$$/ | $$$$$$$$| $$  \__/  | $$    | $$  \ $$| $$  \__/
   | $$   | $$  | $$| $$_____/| $$      | $$ | $$ | $$| $$  | $$  \  $$$/  | $$_____/| $$        | $$ /$$| $$  | $$| $$      
   | $$   | $$  | $$|  $$$$$$$| $$      | $$ | $$ | $$|  $$$$$$/   \  $/   |  $$$$$$$| $$        |  $$$$/|  $$$$$$/| $$      
   |__/   |__/  |__/ \_______/|__/      |__/ |__/ |__/ \______/     \_/     \_______/|__/         \___/   \______/ |__/      
                                                                                                                           
                                            Author:Khaled Al Shamsi  ( V 1.0 )
                """)

print("1     Celsius to fahrenheit convertor")
print("2     Fahrenheit to celsius convertor")
print("3     Kelvin to fahrenheit convertor")
print("4     Fahrenheit to kelvin convertor")
print("5     Kelvin to Celsius convertor")
print("6     Celsius to Kelvin convertor\n")

stng = int(input("Choose your operation settings: "))


#Celsius to fahrenheit convertor
if stng == 1:
    celsius = int(input("Write your Value in Celsius: "))
    def conv_f(u):
        oper = (u * 1.8) + 32
        return oper

    fahrenheit = conv_f(celsius)
    print(fahrenheit)

#Fahrenheit to celsius convertor
elif stng == 2:
    fahrenheit = int(input("Write your Value in Fahrenheit: "))
    def conv_c(u):
        oper = (u - 32) * 0.5555555556
        return oper

    celsius = conv_c(fahrenheit)
    print(celsius)

#Kelvin to fahrenheit convertor
elif stng == 3:
    Kelvin = int(input("Write your Value in Kelvin: "))
    def conv_f(u):
        oper = (u - 273.15) * 1.8 + 32
        return oper

    fahrenheit = conv_f(Kelvin)
    print(fahrenheit)

#Fahrenheit to kelvin convertor
elif stng == 4:
    Fahrenheit = int(input("Write your Value in Fahrenheit: "))
    def conv_k(u):
        oper = (u - 32) * 0.5555555556 + 273.15
        return oper

    kelvin = conv_k(Fahrenheit)
    print(kelvin)

#Kelvin to Celsius convertor
elif stng == 5:
    Kelvin = int(input("Write your Value in Kelvin: "))
    def conv_c(u):
        oper = u - 273.15
        return oper

    celsius = conv_c(Kelvin)
    print(celsius)

#Celsius to Kelvin convertor
elif stng == 6:
    Celsius = int(input("Write your Value in Celsius: "))
    def conv_k(u):
        oper = u + 273.15
        return oper

    kelvin = conv_k(Celsius)
    print(kelvin)

