import math


def calcular_area_circulo(raio):
    return math.pi * raio**2


raio = float(input("Digite o raio do círculo: "))
area = calcular_area_circulo(raio)

print(f"Área do círculo: {area:.2f}")
