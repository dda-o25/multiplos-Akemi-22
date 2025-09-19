"""
Akemi Clarissa Olvera Arao
19/09/25
Con dos números, verificar si uno es múltiplo del otro
"""

# Declaraciones


# Entradas
numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese otro número: "))

# Proceso
if numero_1 % numero_2 == 0:
# Salida
    print("El número ", numero_1, "es múltiplo del número ", numero_2)
# Proceso
elif numero_2 % numero_1 == 0:
# Salida
    print("El número ", numero_2, "es múltiplo del número ", numero_1)
else: 
# Salida
    print("Ninguno de los números es múltiplo del otro")


