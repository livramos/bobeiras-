import random 
#geração de media 
def media (g1):
    if g1== 6:
        fator=1.3
    elif 5.6<= g1 <= 5.9: 
        fator=1.25
    elif 5.0<= g1 <= 5.5: 
         fator=1.2
    elif 4.0<= g1 <= 4.9: 
        fator=1.1
    elif 3.5<= g1 <= 3.9: 
        fator=1.00
    elif 3.0<= g1 <= 3.4: 
        fator=0.9
    elif g1 <3.0: 
        fator= random.uniform(0.75,0.00)
    med= g1*fator 
    return med 


g1=float(input("coloque sua nota de proj int: "))
print(f"sua nota sera: {media(g1)}")
