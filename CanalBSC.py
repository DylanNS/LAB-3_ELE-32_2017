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

def CanalBSC(vetorEntrada, p):
    
    quantMuda = random.binomial(len(vetorEntrada),p)
    
    posicao = random.choice(len(vetorEntrada),quantMuda,replace = False)
    vetorSaida = deepcopy(vetorEntrada)
    for pos in posicao:
        vetorSaida[pos] ^= True
    
    return vetorSaida

vetorEntrada = bitarray(10)
print("vetorEntrada: ",vetorEntrada,"vetorSaida: ",CanalBSC(vetorEntrada,0.5))

def codificadorHamming(vetorEntrada):
    
    G = array([[ 1, 0, 0, 0, 1, 1, 1],[0, 1, 0, 0,1,0,1],
               [0,0,1,0,1,1,0],[0,0,0,1,0,1,1]])
    saida = vetorEntrada.dot(G)
    for i in range(len(saida)):
        
        saida[i] %=2
        
        
    return saida

vetorEntrada = random.randint(0,2,4)
print("VetorEntrada: ",vetorEntrada)
vetorCodificado = codificadorHamming(vetorEntrada)
print("vetor codificado: ", vetorCodificado)

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
        print("Erro! Sindrome eh Vetor Nulo!")
    saida = r+ erro
    for i in range(len(saida)):
        
        saida[i] %=2
    return saida

r = CanalBSC(vetorCodificado,0.2)
print("VEtor recebido: ", r)
estimativa = decodificadorHamming(r)
print("Vetor estimativa do transmitido: ", estimativa)

