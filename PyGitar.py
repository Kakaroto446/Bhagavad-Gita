#!/usr/bin/env python
import os

arq = open('log.txt') #abre arquivp que contem os dados da conta
conteudo = arq.readlines()
arq.close()
verif = ['null\n']
if conteudo[19] == verif[0]: #verifica se ja esta cadastrado
	nome = input('Digite seu nome de usuário: ')
	conteudo[19] = nome
	email = input('Digite seu email: ')
	conteudo[22] = email
	arq = open('log.txt', 'w')
	arq.writelines(conteudo)
	arq.close()

