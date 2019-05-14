#!/usr/bin/env python3

import sys
from collections import Counter
import socket

#1
def num_pacotes():
	i=0
	file = open(sys.argv[1], 'r')
	for line in file:
		i=i+1
	print('1) Numero de pacotes: %s\n' % i)

#2
def top10_IP_src():
	src = []
	file = open(sys.argv[1], 'r')
	for line in file:
		x = line.split(" ")
		if len(x)>12:
			#1 <= dia <= 9
			if x[1]=='':
				src.append(x[12])
			#10 <= dia <= 31
			else:
				src.append(x[11])
	top=conta(src)
	print('2) TOP 10 IPs fonte (IP , Quantidade de pacotes):')
	for i in range (0,10):
		ips=top[i][0]
		ips=ips[4:]
		print(i+1,'\b:', ips,',',top[i][1])
	print()

#3
def top10_IP_dst():
	dst = []
	file = open(sys.argv[1], 'r')
	for line in file:
		x = line.split(" ")
		if len(x)>13:
			#1 <= dia <= 9
			if x[1]=='':
				dst.append(x[13])
			#10 <= dia <= 31
			else:
				dst.append(x[12])
	top=conta(dst)
	print('3) TOP 10 IPs destino (IP , Quantidade de pacotes):')
	for i in range (0,10):
		ips=top[i][0]
		ips=ips[4:]
		print(i+1,'\b:', ips,',',top[i][1])
	print()

#4
def contagem_protocolos():
	prot = []
	file = open(sys.argv[1], 'r')
	for line in file:
		x = line.split(" ")
		if len(x)>19:
			#1 <= dia <= 9
			if x[1]=='':
				if 'DF' in x:
					prot.append(x[20])
				else:
					prot.append(x[19])
			#10 <= dia <= 31
			else:
				if 'DF' in x:
					prot.append(x[19])
				else:
					prot.append(x[18])
	top=conta2(prot)
	print('4) Contagem de pacotes por protocolo (Protocolo , Quantidade de pacotes):')
	for i in range (0,3):
		p=top[i][0]
		p=p[6:]
		print(p,',',top[i][1])
	print()

#5
def top10_portas():
	portas = []
	file = open(sys.argv[1], 'r')
	for line in file:
		x = line.split(" ")
		if len(x)>19 and 'PROTO=ICMP' not in x:
			#1 <= dia <= 9
			if x[1]=='':
				if 'DF' in x:
					portas.append(x[22])
				else:
					portas.append(x[21])
			#10 <= dia <= 31
			else:
				if 'DF' in x:
					portas.append(x[21])
				else:
					portas.append(x[20])
	top=conta(portas)
	print('5) Top 10 portas (Nome , Numero , Quantidade):')
	for i in range (0,10):
		somenteNum= top[i][0]
		somenteNum = somenteNum[4:]
		num = int(somenteNum)
		try:
			print(i+1, '\b:',socket.getservbyport(num),',',num,',',top[i][1])
		except:
			print(i+1, '\b:', '*PORTA NAO REGISTRADA*',',',num,',',top[i][1])
	print()

#Verificar top 10 IPs
def conta(lista):
	lista = Counter(lista)
	lista = list(lista.items())
	lista.sort(key=lambda i: i[1], reverse=True)
	return lista[:10]

#Verificar protocolos
def conta2(lista):
	lista = Counter(lista)
	lista = list(lista.items())
	return lista[:3]

num_pacotes()
top10_IP_src()
top10_IP_dst()
contagem_protocolos()
top10_portas()