#1 — Faça um algoritmo que calcule o valor a ser pago de PIS, COFINS e Lucro de uma empresa
#com base no seu faturamento. A alíquota de PIS é de 0,65% e COFINS 3%, os custo de uma
#empresa deve ser informada pelo usuário. O Lucro é a diferença entre o lucro = faturamento -
#(impostos + custos)
#Exiba na tela o valor do faturamento e os valores:
#Valor do faturamento
#Valor de Imposto PIS
#Valor de COFINS.
#Lucro da empresa

faturamentoBruto = float(input("digite o valor do faturamento"))
custoFuncionario = float(input("digite o salario do seu funcionario"))
custoAluguel = float(input("digite o custo do aluguel"))
pis = 0.65
cofins = 3
descontoPis = (faturamentoBruto / 100) * pis
descontoCofins = (faturamentoBruto / 100) * cofins
custosTotais = (descontoPis + descontoCofins + custoFuncionario + custoAluguel)
lucro = faturamentoBruto - custosTotais
print("faturamento bruto",faturamentoBruto)
print("desconto do pis", descontoPis)
print("desconto cofins", descontoCofins)
print("custos totais", custosTotais)
print("lucro", lucro)
