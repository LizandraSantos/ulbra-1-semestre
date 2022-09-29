#2 - Cada cigarro consumido, o fumante perde em média 15 minutos de vida.
#Faça um algoritmo que leia quantos cigarros são consumidos pelo usuário diariamente e
#há quanto tempo e fumante em meses. Considere que cada mês tenha 30 dias.
#Ao fim mostre quanto tempo ele perderá de vida segundo os dados de entrada.
#E conforme o tempo que o usuário fuma, mostrar as consequências.
#● Se ele fuma há um tempo menor ou igual a 90 dias, dentes amarelos.
#● Tempo entre 90 e 365 dias, perda de paladar e respiração comprometida.
#● Mais que 365 dias, pulmão comprometido.

numerosCigarros = int(input("numero de cigarros por dia"))
tempoDeFumante = int(input("a quanto tempo você fuma em meses"))
tempoEmDias = tempoDeFumante * 30
tempoPerdidoEm1Dia = numerosCigarros * 15
tempoDeVidaPerdido = tempoPerdidoEm1Dia * tempoEmDias
print("baseado nos seus dados você perdeu", tempoDeVidaPerdido)
if tempoDeVidaPerdido <= 90:
    print("dentes amarelos")
elif tempoDeVidaPerdido > 90 and tempoDeVidaPerdido < 365:
    print("perda de paladar e respiraçao comprometida")
elif tempoDeVidaPerdido > 365:
    print("pumao comprometido")   
