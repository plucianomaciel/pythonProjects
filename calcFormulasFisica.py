#!/usr/bin/env python
# coding: utf-8

# In[38]:


while True:
  print("*************************************")    
  print("* CALCULADORA DE FÓRMULAS DE FÍSICA *")
  print("*************************************\n")
  print("cinemática - onde não se preocupamos com a causa do movimento.\n")
  escolha = int(input("escolha qual fórmula quer usar. [1] M.R.U - [2] M.R.U.V\n"))
  
  if escolha == 1:
      print("vamos trabalhar com as fórmulas do Movimento Uniforme.")
      mu = int(input("escolha qual fórmula voce quer. [1] velocidade média [2] aceleração, [3] posição em relação ao espaço\n"))
      
      if mu == 1:
          print("vamos calcular velocidade média\nvelocidade média é a espaço divido pelo tempo\nOBS: insira os dados em km e horas.")
          deltaS = float(input("qual é o espaço percorrido pelo corpo?\n"))
          deltaT = float(input("qual é o tempo que o corpo demorou para percorrer esse espaço?\n"))
          print("A velocidade média foi de  ",deltaS/deltaT,"km/h")
          denovo = int(input("vamos novamente? [1]sim  [2]não\n"))
          
      if mu == 2:
          print("Vamos calular a aceleração de um corpo.\n")
          print("A aceleração é a velocidade dividido pelo tempo\nOBS:a aceleração deve estar em metros e segundos.\n")
          v0 = float(input("Qual é a velocidade inicial V0 em m/s?\n"))
          v1 = float(input("Qual é a velocidade final V1 em m/s?\n"))
          t0 = float(input("Qual é o tempo inicial T0 em segundos?\n"))
          t1 = float(input("Qual é o tempo final T1 em segundos?\n"))
          print("V1-V0 = ",v1-v0)
          print("T1-T0 = ",t1-t0)
          print("A aceleração é de ",(v1-v0)/(t1-t0),"m/s²")
          denovo = int(input("vamos novamente? [1]sim  [2]não\n"))
          
      if mu == 3:
          print("Vamos calcular a posição em relação ao tempo!\n")
          print("Precisamos de 3 dados importantes, a posição inicial a velocidade  e o tempo.\n")
          s0 = float(input("Qual é a posição inicial do corpo em km?\n"))
          Vm = float(input("Qual é a velocidade média do corpo?\n"))
          t = float(input("Qual foi o tempo descrito?\n"))
          print("o espaço percorrido pelo objeto foi de",(Vm*t)-s0,"km")
          denovo = int(input("vamos novamente? [1]sim  [2]não\n"))
          
          if denovo == 1:
              continue
          if denovo == 2:
              break


# In[ ]:





# In[ ]:




