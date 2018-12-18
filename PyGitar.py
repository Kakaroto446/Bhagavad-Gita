#!/usr/bin/env python
import os
import time

arq = open('log.txt') #abre arquivo que contem os dados da conta
conteudo = arq.readlines()
verif = ['null\n']
if conteudo[19] == verif[0]: #verifica se ja esta cadastrado
	nome = input('Digite seu nome de usuário: ')
	conteudo[19] = nome
	#email = input('Digite seu email: ')
	#conteudo[22] = email
	arq = open('log.txt', 'w')
	arq.writelines(conteudo)
	arq.close()

conteudo = [line.rstrip() for line in open('log.txt')]
nome = conteudo[19]
repositorio = input('Digite o nome do repositório: ')
link = ('https://github.com/usuario/repositorio.git')
link = link.replace('usuario', '%s' %nome)
link = link.replace('repositorio', '%s' %repositorio) #aqui o link pra clonar já está pronto

resp = input('Clonar repositorio agora? [sim/nao] ')
if resp == 'sim':
	os.system('git clone %s' %link)
	time.sleep(25)
	os.system('cd %s' %repositorio)
