import os 
os.system("cls||clear")

def calcular_inss(salario):
    if salario <= 1320.00:
        inss = salario * 0.075
    elif salario <= 2571.29:
        inss = salario * 0.09
    elif salario <= 3856.94:
        inss = salario * 0.12
    elif salario <= 7507.49:
        inss = salario * 0.14
    else:
        inss = 1051.05  # Valor máximo permitido

    return min(inss, 1051.05)

def calcular_irrf(salario, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_irrf = salario - deducao_dependentes

    if base_irrf <= 2112.00:
        irrf = 0
    elif base_irrf <= 2826.65:
        irrf = (base_irrf * 0.075)- deducao_dependentes
    elif base_irrf <= 3544.00:
        irrf = (base_irrf * 0.15)- deducao_dependentes
    elif base_irrf <= 4256.00:
        irrf = (base_irrf * 0.2250)- deducao_dependentes
    else:
        irrf = (base_irrf * 0.275) - deducao_dependentes

    return irrf

def main():
    print("=== Sistema de Folha de Pagamento ===")
    
    matricula = input("Digite a matrícula: ")
    senha = input("Digite a senha: ")

    print("\nAcesso autorizado.\n")

    salario_base = float(input("Digite o salário base (R$): "))
    vt_opcao = input("Deseja receber vale transporte? (s/n): ").lower()
    valor_vale_refeicao = float(input("Digite o valor do vale refeição (R$): "))
    
    dependentes = int(input("Se possuir algum dependente, digite quantos sao: "))  # conforme instrução
    plano_saude = (dependentes) * 150.00

    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)

    desconto_vt = salario_base * 0.06 if vt_opcao == 's' else 0
    desconto_vr = valor_vale_refeicao * 0.20

    total_descontos = inss + irrf + desconto_vt + desconto_vr + plano_saude
    salario_liquido = salario_base - total_descontos

    print("\n--- RESUMO DA FOLHA ---")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Total de Descontos: R$ {total_descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()

