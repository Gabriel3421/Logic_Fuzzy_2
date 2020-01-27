
'''
Aluno: Gabriel de Souza Nogueira da Silva
Matricula: 398847

Introduçao sobre o problema:
1-Regras utilizadas:
    • Se atendimento ótimo ou comida deliciosa, então gorjeta alta.
    • Se atendimento aceitável e comida boa, então gorjeta média.
    • Se atendimento péssimo ou comida ruim, então gorjeta baixa.

2- funçoes utilizadas:
    Input:
        Modelo comida
        1- -0.2x +1  [0,5]
        2- 1 - abs((x-5)*0.5) [3,7]
        3- 0.2x -1 [5,10]

        Modelo atendimento
        1- -0.2x +1  [0,5]
        2- 1 - abs((x-5)*0.5) [3,7]
        3- 0.2x -1 [5,10]

    Output
        Modelo gorjeta
        1- -0.1x  + 1 [0,10]
        2- 1-abs((x-14)*1/4) [10,18]
        3- 0.14285714285714285x - 2.571428571428571 [18,25]

'''
import math
import time
import numpy as np
import matplotlib.pyplot as plp

nota_atendimento = 7#int(input("Digite a nota do Atendimento: "))
nota_comida = 8#int(input("Digite a nota da Comida: "))


def atendimento():
    #Definindo as regras de input do atendimento.
    P = -0.2*nota_atendimento+1
    A = 1-abs((nota_atendimento-5)*0.5)
    O = 0.2*nota_atendimento-1

    if P<0:
        P=0
    if A<0:
        A=0
    if O<0:
        O=0
    atend = [P,A,O]
    return atend

def comida():
    #Definindo as regras de input da comida.
    R = -0.2*nota_comida+1
    B = 1-abs((nota_comida-5)*0.5)
    D = 0.2*nota_comida-1
    if R<0:
        R=0
    if B<0:
        B=0
    if D<0:
        D=0        
    co = [R,B,D]
    return co

def regra1():
    #definiçao da regra1 :Se atendimento ótimo ou comida deliciosa, então gorjeta alta.
    gorgeta = [atendimento()[2], comida()[2]]
    gorgeta = max(gorgeta)*2.5#para gerar uma resposta entre 0 e 25 é necessario multiplicar por 2.5                
    return gorgeta

def regra2():
    #definiçao da regra2 :Se atendimento aceitável e comida boa, então gorjeta média.    
    gorgeta = [atendimento()[1], comida()[1]]
    gorgeta = min(gorgeta)*2.5#para gerar uma resposta entre 0 e 25 é necessario multiplicar por 2.5                 
    return gorgeta

def regra3():
    #definiçao da regra3 :Se atendimento péssimo ou comida ruim, então gorjeta baixa.
    gorgeta = [atendimento()[0], comida()[0]]
    gorgeta = max(gorgeta)*2.5#para gerar uma resposta entre 0 e 25 é necessario multiplicar por 2.5             
    return gorgeta

def pa(valor_x):#funçao final, ela dara o valor da reta final para apertar o freio
    alta = regra1()
    media = regra2()
    baixa = regra3()
    #print(alta)    
    #print(media)    
    #print("valor baixa",baixa)    
    if valor_x >=0 and valor_x < 10:
        #print(min(baixa, (-0.1*valor_x +1)))
        return min(baixa, -0.1*valor_x +1)
    
    if valor_x >=10 and valor_x < 18:
        #print(min(media, 1-abs((valor_x-14)*1/4)))
        return min(media, 1-abs((valor_x-14)*1/4))
    if valor_x >=18 and valor_x <= 25:
        #print(min(alta, 0.14285714285714285*valor_x-2.571428571428571))
        return min(alta, 0.14285714285714285*valor_x-2.571428571428571)

def output():
    #utilizando a formula do centro de gravidade temos:
    c1 = 0
    c2 = 0
    for k in range(0,26):#roda de 0 a 25 ao passo de 1 em 1
        c1 = c1 + (pa(k)*k)
     
    for k in range(0,26):#roda de 0 a 25 ao passo de 1 em 1
        c2 = c2 + (pa(k))
        
    c = c1/c2
    print("\n\nValor da Gorgeta: ", c,"\n\n")
    return c #valor com que o freio deve ser apertado dps de se ter analizado as regras

output()

fig, axs = plp.subplots(1, 3, figsize=(50, 4), sharey=True)


fig.suptitle('Logica Fuzzy\n')
axs[0].set_title("Grafico referente ao Atendimento")
x1 = np.outer(np.linspace(0, 5, 10), np.ones(10))
x2 = np.outer(np.linspace(3, 7, 100), np.ones(100))
x3 = np.outer(np.linspace(5, 10, 10), np.ones(10))
y1 = -0.2*x1 +1
y2 = 1 - abs((x2-5)*0.5)
y3 = 0.2*x3 -1
axs[0].plot(x1, y1, color='#2C86AA')
axs[0].plot(x2, y2, color='#2C86AA')
axs[0].plot(x3, y3, color='#2C86AA')
axs[0].axis([0,10,0,1.1])
#plp.show()

axs[1].set_title("Grafico referente a Comida")
axs[1].plot(x1, y1, color='#2C86AA')
axs[1].plot(x2, y2, color='#2C86AA')
axs[1].plot(x3, y3, color='#2C86AA')
axs[1].axis([0,10,0,1.1])
#plp.show()

axs[2].set_title("Grafico referente a Gorgeta")
x1 = np.outer(np.linspace(0, 10, 10), np.ones(10))
x2 = np.outer(np.linspace(10, 18, 100), np.ones(100))
x3 = np.outer(np.linspace(18, 25, 10), np.ones(10))
y1 = -0.1*x1  + 1
y2 = 1 - abs((x2-14)*(1/4))
y3 = 0.14285714285714285*x3-2.571428571428571
axs[2].plot(x1, y1, color='#2C86AA')
axs[2].plot(x2, y2, color='#2C86AA')
axs[2].plot(x3, y3, color='#2C86AA')
axs[2].axis([0,25,0,1.1])
plp.show()