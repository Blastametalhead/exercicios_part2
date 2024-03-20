import os 
os.system ('cls')

print("Algoritmo que lê a idade do usuário e informa a sua classe eleitoral:")
idade = int(input("Digite a sua idade: "))

if idade <1 or idade >120:
 print("ERRO!!!")

elif idade <16:
    print("Não eleitor.")
    
elif idade >=18 and idade <=65:
    print("Eleitor obrigatório.")
    
else: 
  print("Eleitor facultativo.")
  
