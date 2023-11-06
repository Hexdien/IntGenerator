############################################
#
#   Este software irá pedir 2 valores
#   
#   Primeiro pedirá quantos numeros quer gerar
#   Em seguida, quantos caracteres 
#   quer que este numero possua
#
#
#
############################################
import random

 
def numbgen():
  global randN
  global qntdchar
  numb=0
  numbers=""
  while numb <= qntdchar:
    randN=str(random.randint(0,9))
    numb+=1
    numbers+=randN
    if numb == qntdchar:
        
        print(numbers)
        numbers=""
        numb=1
        break
    


try:
  qntd=int(input("Escolha quantos numeros quer gerar: "))
  qntdchar=int(input("Quantos caracteres quer no numero: "))
  if type(qntd) == int and type(qntdchar) == int:
    for _ in range(qntd):
      numbgen()
except:
  print("Tipo de dado inserido não representam números inteiros!! ")
