def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


salario_atual = float(input("Salário atual: R$ ").replace(",", "."))

aumento = salario_atual * 0.15
novo_salario = salario_atual + aumento

print(f"Aumento: R$ {formatar_moeda(aumento)}")
print(f"Novo salário: R$ {formatar_moeda(novo_salario)}")
