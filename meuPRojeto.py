# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:34:48 2017

@author: Dylan N. Sugimoto
"""

from bitarray import bitarray
from copy import deepcopy
from numpy import array
from numpy import array_equal
from numpy import random

def CanalBSC(vetorEntrada, p):
    quantMuda = random.binomial(len(vetorEntrada), p)
    posicao = random.choice(len(vetorEntrada), quantMuda, replace = False)
    vetorSaida = deepcopy(vetorEntrada)

    for pos in posicao:
        vetorSaida[pos] ^= True

    return vetorSaida,quantMuda

def codificadorHamming(vetorEntrada):
    g1 =  array([1,0,0,0,0,0,0,0,0,0,0,1,1,1,1])
    g2 =  array([0,1,0,0,0,0,0,0,0,0,0,1,1,1,0])
    g3 =  array([0,0,1,0,0,0,0,0,0,0,0,1,1,0,1])
    g4 =  array([0,0,0,1,0,0,0,0,0,0,0,1,1,0,0])
    g5 =  array([0,0,0,0,1,0,0,0,0,0,0,1,0,1,1])
    g6 =  array([0,0,0,0,0,1,0,0,0,0,0,1,0,1,0])
    g7 =  array([0,0,0,0,0,0,1,0,0,0,0,1,0,0,1])
    g8 =  array([0,0,0,0,0,0,0,1,0,0,0,0,1,1,1])
    g9 =  array([0,0,0,0,0,0,0,0,1,0,0,0,1,1,0])
    g10 = array([0,0,0,0,0,0,0,0,0,1,0,0,1,0,1])
    g11 = array([0,0,0,0,0,0,0,0,0,0,1,0,0,1,1])
    G = array([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11])
    saida = vetorEntrada.dot(G)

    for i in range(len(saida)):
        saida[i] %=2

    return saida

#vetorEntrada = random.randint(0,2,11)
#print("VetorEntrada: ",vetorEntrada)
#vetorCodificado = codificadorHamming(vetorEntrada)
#print("vetor codificado: ", vetorCodificado)

def calculaSindrome(r):
    h1 =  array([1, 1, 1, 1])
    h2 =  array([1, 1, 1, 0])
    h3 =  array([1, 1, 0, 1])
    h4 =  array([1, 1, 0, 0])
    h5 =  array([1, 0, 1, 1])
    h6 =  array([1, 0, 1, 0])
    h7 =  array([1, 0, 0, 1])
    h8 =  array([0, 1, 1, 1])
    h9 =  array([0, 1, 1, 0])
    h10=  array([0, 1, 0, 1])
    h11 = array([0, 0, 1, 1])
    h12 = array([1, 0, 0, 0])
    h13 = array([0, 1, 0, 0])
    h14 = array([0, 0, 1, 0])
    h15 = array([0, 0, 0, 1])
    H = array([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15])
    s = r.dot(H)

    for i in range(len(s)):
        s[i] %=2

    return s

def MapErro(s):
    h1 =  array([1, 1, 1, 1])
    h2 =  array([1, 1, 1, 0])
    h3 =  array([1, 1, 0, 1])
    h4 =  array([1, 1, 0, 0])
    h5 =  array([1, 0, 1, 1])
    h6 =  array([1, 0, 1, 0])
    h7 =  array([1, 0, 0, 1])
    h8 =  array([0, 1, 1, 1])
    h9 =  array([0, 1, 1, 0])
    h10=  array([0, 1, 0, 1])
    h11 = array([0, 0, 1, 1])
    h12 = array([1, 0, 0, 0])
    h13 = array([0, 1, 0, 0])
    h14 = array([0, 0, 1, 0])
    h15 = array([0, 0, 0, 1])
    e = array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    if(array_equal(s, h1)):
        e[0] = 1
    elif(array_equal(s, h2)):
        e[1] = 1
    elif(array_equal(s, h3)):
        e[2] = 1
    elif(array_equal(s, h4)):
        e[3] = 1
    elif(array_equal(s, h5)):
        e[4] = 1
    elif(array_equal(s, h6)):
        e[5] = 1
    elif(array_equal(s, h7)):
        e[6] = 1
    elif(array_equal(s, h8)):
        e[7] = 1
    elif(array_equal(s, h9)):
        e[8] = 1
    elif(array_equal(s, h10)):
        e[9] = 1
    elif(array_equal(s, h11)):
        e[10] = 1
    elif(array_equal(s, h12)):
        e[11] = 1
    elif(array_equal(s, h13)):
        e[12] = 1
    elif(array_equal(s, h14)):
        e[13] = 1
    elif(array_equal(s, h15)):
        e[14] = 1
    return e

def decodificadorHamming(r):
    s = calculaSindrome(r)

    if(array_equal(s, array([0, 0, 0, 0]))):
        print("Sindrome é vetor nulo!")

    erro = MapErro(s)
    saida = r + erro
    for i in range(len(saida)):
        saida[i] %=2

    return saida

#------------------------------------------------------------------------------
#Funcoes para coleta de dados
#------------------------------------------------------------------------------

# Gera múltiplos arrays binários aleatório
def RandomNumberGenerator(quantVetores):
    dic = {}

    for i in range(quantVetores):
        dic[i] = random.randint(0, 2, 11)

    return dic

def PassarNoCanalBSC(dic, p):
    resposta = {}
    quantMudado = 0

    for key in dic:
      resposta[key], mudou = CanalBSC(dic.get(key), p)
      quantMudado += mudou

    return resposta,quantMudado

def PassarNoCodificador(dic):
    amostraCodificada = {}

    for key in dic:
        amostraCodificada[key] = codificadorHamming(dic.get(key))

    return amostraCodificada

def PassarNoDeCodificador(dic):
    amostraDecodificada = {}

    for key in dic:
        amostraDecodificada[key] = decodificadorHamming(dic.get(key))

    return  amostraDecodificada

def ContarErros(decodificada,original):
    quantErro = 0

    for i in range(len(original)):
        for j in range(11):
            if(not decodificada[i][j] == original[i][j]):
                quantErro +=1

    return quantErro

#------------------------------------------------------------------------------
#Coleta de dados

Pe ={} #probabilidade de erro depois de decodificado
Ps = {} # probabilidade de erro sem codificar
Pc = {} # probabilidade de erro com codificacao
milhaobits = pow(10,6)
p = 0.5
totalerro = 0
for i in range(10):
    quantVetores = int(250000)
    dic = RandomNumberGenerator(quantVetores)
    amostraAlterada,quantMudado = PassarNoCanalBSC(dic,p)
    Ps[i] = quantMudado/(250000*11)
    amostraCodificada = PassarNoCodificador(dic)
    amostraCodificadaAlterada,quantMudado = PassarNoCanalBSC(amostraCodificada,p)
    Pc[i] = quantMudado/(250000*15)
    amostraDecodificada = PassarNoDeCodificador(amostraCodificadaAlterada)
    quantErro = ContarErros(amostraDecodificada,amostraCodificada)
    Pe[i] = quantErro/(250000*11)
    totalerro += quantErro

Psmedia =0
Pcmedia =0
Pemedia =0
for i in range(10):
    Psmedia += Ps.get(i)
    Pcmedia += Pc.get(i)
    Pemedia += Pe.get(i)

print("p = ",p)
print("Probabilidade de erro: ",(Pemedia/10),"\nProbabilidade de erro sem codificacao: ",Psmedia/10)
print("Probabilidade de erro com codificacao: ", Pcmedia/10)
print("QUantidade de erro: ",totalerro)
