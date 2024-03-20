import os 
os.system ('cls')

print("Algoritmo no qual informa o cargo do funcionário conforme o código")
codigo = int(input("Digite o código do cargo: "))

if codigo ==1:
  print("Escritutário.")
if codigo ==2: 
    print("Secretária.")
if codigo ==3: 
    print("Caixa.")
if codigo ==4: 
    print("Gerente.")
if codigo ==5: 
    print("Diretor.")
    
else:
 print("Código inexistente. ")