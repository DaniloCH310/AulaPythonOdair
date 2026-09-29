x = 10  # Variável global


def alterar_valor():
    x = 5  # Variável local
    print(f"Valor dentro da função: {x}")


alterar_valor()
print(f"Valor fora da função: {x}")

# Resposta A:
# Valor dentro da função: 5
# Valor fora da função: 10

# Resposta B:
# O x criado dentro da função possui escopo local e só existe dentro dela.
# O x que vale 10 possui escopo global. Como a função não altera a variável
# global, o valor de x fora da função continua sendo 10.
