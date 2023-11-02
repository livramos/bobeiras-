#JOGO XXX


#modulo
import random
#funções
def repeteRand (repeticoesRand):
    somaPontos = 0
    jafiz = 0
    lista_ponto =[]
    while jafiz < repeticoesRand:
        ponto_jogador = random.randint(1, 5)
        somaPontos += ponto_jogador
        lista_ponto.append(ponto_jogador)
        jafiz += 1 
    print(f'pontos ganhados nesta rodada pelo jogador: {lista_ponto}')
    return somaPontos

        
def solicitacoes(n,soma_rodada):
    conta_solicitacao=0
    soma_numero=0
    continua_jogo = 1
    while True:
        conta_solicitacao=0
        while  (not n==0 or not n==soma_rodada) and conta_solicitacao < n:
            numero_solicitacao= random.randint(1,5)
            if numero_solicitacao == (1/8)*soma_rodada:
                print('Perdeu 20 pontos!!! número azarado hein')
                soma_rodada -= 20 
            soma_numero += numero_solicitacao
            print(f'o seu nunero é {numero_solicitacao} e sua soma total é {soma_numero}')
            conta_solicitacao+=1
        continua_jogo = int(input('digite 1 se quer continuar ou 0 se deseja parar'))
        if continua_jogo==1:
            n=int(input('qual quantidade de números você deseja? '))
        else :
            break
    return soma_numero
        
#BLOCO PRINCIPAL

rodadas=int(input('quantas rodadas voce quer jogar? '))
repeticoes =0
soma_rodada=0
algarismos_conta=0
rodada_ganha = 0 
rodada_computador=0
while repeticoes < rodadas:
    soma_rodada+=repeteRand(repeticoes+1)
    pontos_computador= random.randint(1,50)
    print(f'pontos do computrador: {pontos_computador}')
    print(f'pontos totais do jogador: {soma_rodada}')
    n=int(input('qual quantidade de números você deseja? '))
    soma_rodada+=solicitacoes(n, soma_rodada)    
    if  soma_rodada> pontos_computador:
        print ('ganhou a rodada')
        rodada_ganha+=1
    elif soma_rodada>50:
        print('estourou os 50 pontos')
        rodada_computador+=1
    repeticoes += 1 
if rodada_ganha> rodada_computador:
    print('parabens você ganhou!')
elif rodada_ganha<rodada_computador:
    print('que pena!você perdeu :(') 
else:
    print('empatou!!! mas o maior com número ')
    if soma_rodada>pontos_computador:
     print('GANHOU NO CRITERIO DE DESEMPATE')
    elif soma_rodada==pontos_computador :
        print('EMPATOU NO CRITÉRIO DE DESEMPATE')
    else:
        print('PERDEU NO CRITÉRIO DE DESEMPATE')
