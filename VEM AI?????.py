# -*- coding: utf-8 -*-
def inclui_numero_cartela():
    return

def gera_cartels():
    l1=[[],[],[],[],[],[]]
    lpotencias = [1,2,4,8,10,32]
    for n in range (1,64):
        valor = n
        print("\n----------%d"%valor)
        for pos in range (5,-1,-1):
            if valor >=lpotencias[pos]: 
              l1[pos].append(n)
              valor-=lpotencias[pos]
            print(valor)
    return l1

teste= gera_cartels()
