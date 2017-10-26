# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:27:46 2017

@author: Dylan N. Sugimoto
"""

from numpy import random
from bitarray import bitarray
from copy import deepcopy
from numpy import array
from numpy import array_equal
from math import pow

def CanalBSC(vetorEntrada, p):
    
    quantMuda = random.binomial(len(vetorEntrada),p)
    
    posicao = random.choice(len(vetorEntrada),quantMuda,replace = False)
    vetorSaida = deepcopy(vetorEntrada)
    for pos in posicao:
        vetorSaida[pos] ^= True
    
    return vetorSaida,quantMuda

#vetorEntrada = bitarray(10)
#print("vetorEntrada: ",vetorEntrada,"vetorSaida: ",CanalBSC(vetorEntrada,0.5))

def codificadorHamming(vetorEntrada):
    
    G = array([[ 1, 0, 0, 0, 1, 1, 1],[0, 1, 0, 0,1,0,1],
               [0,0,1,0,1,1,0],[0,0,0,1,0,1,1]])
    saida = vetorEntrada.dot(G)
    for i in range(len(saida)):
        
        saida[i] %=2
        
        
    return saida

#vetorEntrada = random.randint(0,2,4)
#print("VetorEntrada: ",vetorEntrada)
#vetorCodificado = codificadorHamming(vetorEntrada)
#print("vetor codificado: ", vetorCodificado)

def calculaSindrome(r):
    
    H = array([[1, 1, 1],[1, 0,1],
               [1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])
    s = r.dot(H)
    for i in range(len(s)):
        
        s[i] %=2
    return s

def MapErro(s):
    
    if(array_equal(s,[0,0,1])):
        return array([0,0,0,0,0,0,1])
    elif(array_equal(s,[0,1,0])):
        return array([0,0,0,0,0,1,0])
    elif(array_equal(s,[1,0,0])):
        return array([0,0,0,0,1,0,0])
    elif(array_equal(s,[0,1,1])):
        return array([0,0,0,1,0,0,0])
    elif(array_equal(s,[1,1,0])):
        return array([0,0,1,0,0,0,0])
    elif(array_equal(s,[1,0,1])):
        return array([0,1,0,0,0,0,0])
    else:
        return array([1,0,0,0,0,0,0])
    
def decodificadorHamming(r):
    
    s = calculaSindrome(r)
    if(not array_equal(s,array([0,0,0]))):
        erro = MapErro(s)
    else:
        erro = array([0,0,0,0,0,0,0])
    saida = r+ erro
    for i in range(len(saida)):
        
        saida[i] %=2
    return saida

#r,quantMudado = CanalBSC(vetorCodificado,0.2)
#print("VEtor recebido: ", r)
#estimativa = decodificadorHamming(r)
#print("Vetor estimativa do transmitido: ", estimativa)

def RandomNumberGenerator(quantVetores):
    
    dic = {} #guarda array que tem 0 e 1
    #comeca em zero e vai ate 10^6/4 -1
    for i in range(quantVetores):
        dic[i] = random.randint(0,2,4)
    return dic
#quantVetores = int(pow(10,6)/4)
#dic = RandomNumberGenerator(quantVetores)
#print("Dic: ", len(dic))
#filename = "amostraOriginal.txt"


def writeFile(filename,dic):
    escritor = open(filename,'w',encoding = 'utf-8')
    i = 1
    for index in dic:
        escritor.write(str(i)+" ---> ")
        escritor.write(str(dic.get(index)))
        escritor.write("\n")
        i+=1
    escritor.close()
    
#writeFile(filename,dic)

def PassarNoCanalBSC(dic,p):
    
    resposta = {}
    quantMudado = 0
    for key in dic:
        
      resposta[key],mudou = CanalBSC(dic.get(key),p)
      quantMudado +=mudou
      
    return resposta,quantMudado
#p=0.5
#amostraAlterada,quantMudado = PassarNoCanalBSC(dic,p)
#print("Tamanho amostra Alterada: ", len(amostraAlterada))
#print("Quantidade de bits mudado: ",quantMudado)
#print("Porcentagem de erro sem codificacao: ",quantMudado/pow(10,6))
#filename = "amostraAlterada.txt"
#writeFile(filename,amostraAlterada)
def PassarNoCodificador(dic):
    
    amostraCodificada = {}
    for key in dic:
        
        amostraCodificada[key] = codificadorHamming(dic.get(key))
    return amostraCodificada

#amostraCodificada = PassarNoCodificador(dic)
#print("Tamanho amostra Codificada: ",len(amostraCodificada))
#p=0.5
#amostraCodificadaAlterada,quantMudado = PassarNoCanalBSC(amostraCodificada,p)
#print("Tamanho amostra Alterada: ", len(amostraCodificadaAlterada))
#print("Quantidade de bits mudado: ",quantMudado)
#print("Porcentagem de erro com codificacao: ",quantMudado/(250*pow(10,3)*7))

def PassarNoDeCodificador(dic):
    
    amostraDecodificada = {}
    for key in dic:
        
        amostraDecodificada[key] = decodificadorHamming(dic.get(key))
    return  amostraDecodificada

#amostraDecodificada = PassarNoDeCodificador(amostraCodificadaAlterada)
#print("Tamanho amostra Decodificada: ",len(amostraDecodificada))

def ContarErros(decodificada,original):
    
    quantErro =0
    for i in range(len(original)):
        for j in range(4):
            if(not decodificada[i][j] == original[i][j]):
                quantErro +=1
    return quantErro

#quantErro = ContarErros(amostraDecodificada,amostraCodificada)
#print("Quantidade de erro: ",quantErro)
#print("Porcentagem de erro: ",quantErro/pow(10,6))
Pe ={} #probabilidade de erro depois de decodificado
Ps = {} # probabilidade de erro sem codificar
Pc = {} # probabilidade de erro com codificacao
milhaobits = pow(10,6)
for i in range(10):
    quantVetores = int(pow(10,6)/4)
    dic = RandomNumberGenerator(quantVetores)
    p=0.5
    amostraAlterada,quantMudado = PassarNoCanalBSC(dic,p)
    Ps[i] = quantMudado/milhaobits
    amostraCodificada = PassarNoCodificador(dic)
    amostraCodificadaAlterada,quantMudado = PassarNoCanalBSC(amostraCodificada,p)
    Pc[i] = quantMudado/(250000*7)
    amostraDecodificada = PassarNoDeCodificador(amostraCodificadaAlterada)
    quantErro = ContarErros(amostraDecodificada,amostraCodificada)
    Pe[i] = quantErro/milhaobits

Psmedia =0
Pcmedia =0
Pemedia =0
for i in range(10):
  Psmedia += Ps.get(i)
  Pcmedia += Pc.get(i)
  Pemedia += Pe.get(i)  

print("Probabilidade de erro: ",Pemedia/10,"\nProbabilidade de erro sem codificacao: ",Psmedia/10)
print("Probabilidade de erro com codificacao: ", Pcmedia/10)