import math


def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)


cateto_a = float(input("Digite o valor do primeiro cateto: "))
cateto_b = float(input("Digite o valor do segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
print(f"Hipotenusa: {hipotenusa:.2f}")
