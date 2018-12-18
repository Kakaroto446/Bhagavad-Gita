#!/usr/bin/env python
import os

#arq = open('log.txt') #abre arquivo que contem os dados da conta
#conteudo = arq.readlines()
#verif = ['null\n']
#if conteudo[19] == verif[0]: #verifica se ja esta cadastrado
#os.system('nano log.txt')

conteudo = [line.rstrip() for line in open('log.txt')]
nome = conteudo[19]
email = conteudo[22]
repository = conteudo[25]

prosseguir = input('Clonar repositório? ')
if prosseguir == 'sim':
	link = ('https://github.com/usuario/repositorio.git')
	link = link.replace('usuario', '%s' %nome)
	link = link.replace('repositorio', '%s' %repository)

print(link)
