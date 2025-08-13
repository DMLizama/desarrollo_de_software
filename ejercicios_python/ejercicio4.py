def convertir_a_Fahrenheit (temp):
    temp = (temp - 32) * 5/9
    return f"Los Celsius ingresados son {temp:.2f}°F"

def convertir_a_Celsius (temp):
    temp = (temp * 9/5) + 32
    return f"Los Fahrenheit ingresados son {temp}°C"

value = float(input("Ingrese la temperatura: "))
condition = 0
while condition == 0:
    scale=str(input("Ingrese la escala (C o F) para convertir el valor: "))
    if scale == 'C' or scale == 'c':
        condition = 1
        print(convertir_a_Fahrenheit(value))
    elif scale == 'F' or scale == 'f':
        condition = 1
        print(convertir_a_Celsius(value))