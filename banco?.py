#Metodos
import os 
#Variaveis
arq_senhas = open('senhas.txt', 'a+')
arq_emails = open('emails.txt', 'a+')
#Funções 
def criaConta():
  email = input('Insira um email: ')
  senha = input('Insira uma senha: ')
  arq_emails.write(email)
  arq_emails.write('\n')
  arq_senhas.write(senha)
  arq_senhas.write('\n')
  arq_senhas.close()
  arq_emails.close()
  print('Conta Criada com sucesso!')
  return

def aceita_email(variavel): 
    
    return 
    
    
    
def Verifica_log(arq,variavel):
  arquivo = open(arq,'r')
  for linha in arquivo:
    linha=linha.strip()
    if linha == variavel:
      return True
  arquivo.close()
  return False



#blocoPrincipal 

tem_Conta=input('Já tem conta? ')
if tem_Conta == 'sim':
  email= input('Coloque seu email: ')
  senha= input('Coloque sua senha: ')
  if Verifica_log('emails.txt', email) and Verifica_log('senhas.txt', senha):
    input('Logado com sucesso!')
  else:
    print('Senha ou email incorretos. Tente novamente.')

else: 
    criaConta()


arq_senhas.close()
arq_emails.close()

os.system('cls')  
# interface do banco 

print(' Bem vindo ao banco 100% veridico')

