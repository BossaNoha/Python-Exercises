class Main:
    def TemperatureConverter(self):
        user_input = input("pick one of desired conversions (type it in this exact form): c-f / f-c / c-k - k-c\n")
        original_temperature = float(input("temperature to be converted\n"))
        if user_input == "c-f":
            converted_temperature = original_temperature*9/5+32
            temp_type = "°K"
        elif user_input == "f-c":
            converted_temperature = (original_temperature-32)*5/9
            temp_type = "°C"
        elif user_input == "c-k":
            converted_temperature = original_temperature + 273.15
            temp_type = "°K"
        elif user_input == "k-c": 
            converted_temperature = original_temperature - 273.15
            temp_type = "°C"
        else: converted_temperature = "invalid input"
        return converted_temperature, temp_type

main = Main()
own_converter, temp_type = main.TemperatureConverter()
print (own_converter, temp_type)
