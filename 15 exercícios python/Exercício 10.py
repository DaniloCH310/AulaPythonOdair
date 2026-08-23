def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


salario_fixo = float(input("Salário fixo: R$ ").replace(",", "."))
total_vendido = float(input("Total vendido: R$ ").replace(",", "."))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

print(f"Comissão: R$ {formatar_moeda(comissao)}")
print(f"Salário total: R$ {formatar_moeda(salario_total)}")
