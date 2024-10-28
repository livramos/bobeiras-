# codigo pra fazer os calculos de freio do baja 
# versão 1.2
#import 
import math 
pi=math.pi
#funções 
#calculo do pedal ratio
def PR (diametro_menor, diametro_maior):
     return diametro_menor / diametro_maior

#calculo da forca do pedal 
def forca ( forca_aplicada, pr):
    return forca_aplicada * pr  

# BB (formula da porcentagem transmitida para o blance bar)
def BB(med_dianteiro,med_traseiro):
    return med_dianteiro / (med_dianteiro + med_traseiro)

#Forca aplicada no cilindro (vou apelidar de FAC)
def FAC(forca_pedal,pedal_ratio,BB):
    Fac_diant= forca_pedal*pedal_ratio*BB
    Fac_tras= forca_pedal*pedal_ratio*(1-BB)
    return Fac_diant,Fac_tras
#principio de pascal 
def pascal (diametro_pistão_menor, diametro_pistão_maior):
    return (diametro_pistão_maior/diametro_pistão_menor)**2
#calculo da força nas pinças (F_pincas)
def F_pincas (forca_aplicada, pedal_ratio, BB,pascal):
    return forca_aplicada * pedal_ratio * BB * pascal
#calculo da pressão da linha
def pressao_linha (forca_aplicada,pedal_ratio,BB,pascal):
    return forca_aplicada * pedal_ratio * BB /(pi*pascal) 
# funções de exibição 
def exibe_distancia():
    distancia_menor=float(input("Digite a distancia entre o ponto de giro e o balance bar em cm (EXEMPLO: 10.0)"))
    distancia_maior=float(input("Agora digite a distancia entre o ponto de giro até a onde o pé é aplicado em cm (EXEMPLO: 10.0)"))
    return (distancia_menor,distancia_maior)
def exibe_forca():
    F_aplicada=float(input("digite a força aplicada no pedal em N (EXEMPLO: 100.0)"))
    return F_aplicada
def exibe_medida():
    medida_dianteira=float(("Digite a distancia do ponto de giro do cilindro mestre dianteiro até o ponto central do balance bar em cm (EXEMPLO: 10.0)"))
    medida_traseira=float(("Digite a distancia do ponto de giro do cilindro mestre traseiro até o ponto central do balance bar em cm (EXEMPLO: 15.0)"))
    return medida_dianteira,medida_traseira
def exibe_pistao():
    print("Digite o diametro do pistão menor em mm (EXEMPLO: 10.0)")
    diametro_menor = float(input(" "))
    print("Digite o diametro do pistão maior em mm (EXEMPLO: 15.0)")
    diametro_maior = float(input(" "))
    return diametro_menor,diametro_maior
def exibe_pinca():
    print("Digite o diametro do pistão do cilindro mestre dianteiro em mm (EXEMPLO: 10.0)")
    diam_menor_dianteira = float(input(" "))
    print("digite o diametro do pistão do cilindro mestre traseiro em mm (EXEMPLO: 10.0)")	
    diam_maior_traseira = float(input(" "))
    return diam_menor_dianteira,diam_maior_traseira
#bloco principal 
escolha=int(input("Escreva quais contas precisam ser realizadas: \n 1 - Pedal Ratio \n 2 - Força do pedal \n 3 - Balance Bar \n 4-Força aplicada no cilindro mestre \n 5-Pascal \n6-Força nas pinças \n 7-pressão da linha \n8 - Todas as contas"))
if (escolha ==1):  
    #chamando para o calculo do pedal ratio 
    exibe_distancia()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    print("O pedal ratio é: ", PR_real)
elif (escolha==2): 
     #chamando para o calculo do pedal ratio 
    exibe_distancia()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    #realizando o calculo da força do pedal 
    exibe_forca()
    #força do pedal feita 
    forca_real = forca(F_aplicada, PR_real) 
    #mostrando o resultado
    print("a força no pedal será: ", forca_real)
    print("O pedal ratio é: ", PR_real)
elif (escolha==3):
    #chamando para o calculo do balance bar
    exibe_medida()
    #fazendo o calculo de BB
    BB_real_dianteiro = BB(medida_dianteira, medida_traseira)
    BB_real_traseiro = 1 - BB_real_dianteiro
    #exibindo resuldado 
    print("A porcentagem de força transmitida para o cilindro mestre dianteiro é %.2f \n Enquanto a porcentagem transmitida para o traseiro é: %.2f", BB_real_dianteiro, BB_real_traseiro)
elif(escolha==4):
 #chamando para o calculo do pedal ratio 
    exibe_distancia()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    #chamando para o calculo do balance bar
    exibe_medida()
    #fazendo o calculo de BB
    BB_real_dianteiro = BB(medida_dianteira, medida_traseira)
    #pegando os dados da força aplicada no pedal 
    exibe_forca()
    #realizando o calculo da FAC
    Fac_diant, Fac_tras =FAC(F_aplicada, PR_real,BB_real_dianteiro)
    #mostrando o resultado
    print("A força aplicada no cilindro mestre dianteiro é: %.2f \n E a traseira é %.2f ", Fac_diant,Fac_tras)
elif (escolha==5):
    #chamando para o calculo de pascal (pegando os dados do usuario)
    exibe_pistao()
    #aplicando a função (formula de pascal)
    pascal_real = pascal(diametro_menor, diametro_maior)
    #mostrando o resultado
    print("o resuldado é %.2f",pascal_real)
elif (escolha==6):
    #coletando as informações 
    exibe_forca()
    exibe_distancia()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    exibe_medida()
    #fazendo o calculo de BB
    BB_real_dianteiro = BB(medida_dianteira, medida_traseira)
    BB_real_traseiro = 1 - BB_real_dianteiro
    exibe_pistao()
    exibe_pinca()
    #aplicando a função (formula de pascal)
    pascal_dianteira= pascal(diam_menor_dianteira, diam_maior_dianteira) *2
    pascal_traseira= pascal(diam_menor_traseira, diam_maior_traseira) 
    #realizando o calculo da força nas pinças
    F_pincas_dianteira = F_pincas(F_aplicada, PR_real, BB_real_dianteiro, pascal_dianteira)
    F_pincas_traseira = F_pincas(F_aplicada, PR_real, BB_real_traseiro, pascal_traseira)
    #mostrando o resultado
    print("A força nas pinças dianteiras é: %.2f \n E a traseira é %.2f ", F_pincas_dianteira,F_pincas_traseira)
elif (escolha==7):
    #coletando as informações 
    exibe_forca()
    exibe_distancia()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    exibe_medida()
    #fazendo o calculo de BB
    BB_real_dianteiro = BB(medida_dianteira, medida_traseira)
    BB_real_traseiro = 1 - BB_real_dianteiro
    #pegando os dados do cilindro
    exibe_pinca()
    #aplicando a função (formula de pascal)
    pascal_dianteira=pascal(diam_cilindro_dianteira,2)
    pascal_traseira=pascal(diam_cilindro_traseira,2)
    #realizando o calculo da pressão da linha
    pressao_dianteira = pressao_linha(F_aplicada, PR_real, BB_real_dianteiro, pascal_dianteira)
    pressao_traseira = pressao_linha(F_aplicada, PR_real, BB_real_traseiro, pascal_traseira)
    #mostrando o resultado
    print("A pressão na linha dianteira é: %.2f \n E a traseira é %.2f ", pressao_dianteira,pressao_traseira)
elif (escolha==8):
    exibe_medida()
    #pedal ratio feito 
    PR_real = PR(distancia_menor, distancia_maior)
    print("O pedal ratio é: ", PR_real)
     #realizando o calculo da força do pedal 
    exibe_forca()
    #força do pedal feita 
    forca_real = forca(F_aplicada, PR_real) 
    #mostrando o resultado
    print("a força no pedal será: ", forca_real)
     #chamando para o calculo do balance bar
    exibe_distancia()
    #fazendo o calculo de BB
    BB_real_dianteiro = BB(medida_dianteira, medida_traseira)
    BB_real_traseiro = 1 - BB_real_dianteiro
    #exibindo resuldado 
    print("A porcentagem de força transmitida para o cilindro mestre dianteiro é %.2f \n Enquanto a porcentagem transmitida para o traseiro é: %.2f", BB_real_dianteiro, BB_real_traseiro)
     #realizando o calculo da FAC
    Fac_diant, Fac_tras =FAC(F_aplicada, PR_real,BB_real_dianteiro)
    #mostrando o resultado
    print("A força aplicada no cilindro mestre dianteiro é: %.2f \n E a traseira é %.2f ", Fac_diant,Fac_tras)
     #chamando para o calculo de pascal (pegando os dados do usuario)
    exibe_pistao()
    #aplicando a função (formula de pascal)
    pascal_real = pascal(diametro_menor, diametro_maior)
    #mostrando o resultado
    print("o resuldado é ",pascal_real)
else:
    print("opção invalida")