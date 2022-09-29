#4. A clínica PicaPau de hemodiálise realiza acompanhamento e tratamento de 110 pacientes
#renais crônicos de várias cidades do litoral norte do RS. Os pacientes realizam sessões de
#hemodiálise 3 vezes na semana, sendo que, cada sessão dura entre 2 a 4 horas conforme a
#diferença entre o peso seco e o peso atual.
#Faça um programa para calcular o peso seco de um paciente que está realizando hemodiálise. E
#o tempo que ele irá ficar em sessão de hemodiálise.
#Considere o peso seco: o resultado do seu balanço hídrico, ou seja, o peso sem edema,
##descontando os valores de líquidos ingeridos deste paciente em 24h. Utilize a seguinte fórmula:
#peso seco = Peso atual - quantidade de líquidos ingeridos nas últimas 24 h.
#Mostre a diferença entre esses valores: peso seco e peso atual para calcular o tempo de
#sessão de cada paciente e mostre quanto tempo pode ser a sessão de hemodiálise conforme a
#tabela.
#peso seco for > 1 and < 2 = 2h
#peso seco for > 2 and < 3 = 3h
#peso seco for > 3 = 4h

pesoDoPaciente = float(input("informe seu peso"))
qtdLiquidos24h = float(input("quantidade de líquidos ingeridos nas últimas 24h"))
pesoSeco = pesoDoPaciente - qtdLiquidos24h
if pesoSeco > 1 and pesoSeco < 2:
    print("tempo de duraçao 2h")
elif pesoSeco > 2 and pesoSeco < 3:
    print("tempo de duraçao 3h")
elif pesoSeco > 3:
    print("tempo de duraçao 4h")
    
