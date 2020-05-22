from math import sqrt
"""
Cap 11 - Dicionarios
1. Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a
cor da camisa que está usando como valor.
"""
pessoas = {
    'Pedro': 'Azul',
    'Miguel': 'Amarelo',
    'Claudia': 'Verde',
    'Marta': 'Verde',
    'Alexandre': 'Azul Claro'
}

print('EXERCICIO 5')
print('CAP 11')
print('q1.')
print(f'Dicionario pessoas = {pessoas}')

"""
2. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da
semana, tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e
domingo recebem listas vazias, ou você tem aula?).
"""
semana = {}
semana.update(segunda=['OEM para análise de sistemas',
                       'Sociologia aplicada a informatica'])
semana.update(terca=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(quarta=['OEM para análise de sistemas'])
semana.update(quinta=['Computacao grafica', 'Sistemas distribuidos'])
semana.update(sexta=['Desenvolvimento Web em Python', 'Java avancado'])
semana.update(sabado=[])
semana.update(domingo=[])

print('\nq2.')
print(f'Dicionario semana = {semana}')

"""
3. Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como
valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado.
Preencha 5 filmes.
"""
filmes = {}
filmes['O silencio dos inocentes'] = {
    'vilao': 'Hannibal Lecter',
    'ano': '1991'
}
filmes['Psicose'] = {
    'vilao': 'Norman Bates',
    'ano': '1960'
}
filmes['Gladiador'] = {
    'vilao': 'Lucius Aurelius Commodus',
    'ano': '2000'
}
filmes['Hellraiser'] = {
    'vilao': 'Pinhead',
    'ano': '1987'
}
filmes['Senhor dos Aneis: A sociedade do anel'] = {
    'vilao': 'Sauron',
    'ano': '2001'
}

print('\nq3.')
# Me recuso a colocar alguns como vilões, tipo Darth Vader ou Coringa...:)
print(f'Dicionario filmes = {filmes}')

"""
Cap 13 - Estruturas de Controle

1. Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.
"""
print('\nCAP 13')
print('q1.')
numero_1 = int(input('Informe o um número: '))
numero_2 = int(input('Informe outro um número: '))
while numero_2 == numero_1:
	numero_2 = int(input('O numero nao pode ser igual ao primeiro! Informe outro numero: '))

if numero_1 > numero_2:
    menor = numero_2
elif numero_1 < numero_2:
    menor = numero_1

print(f'O menor numero entre {numero_1} e {numero_2} é: {menor}')

"""
2. Para doar sangue é necessário :
• Ter entre 16 e 69 anos.
• Pesar mais de 50 kg.
• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela
pode doar sangue ou não.
"""
print('\nq2.')
def verificador(valor, min, max, msg:str ):
	while valor<min or valor>max:
		tipo = type(valor)
		valor = input(f'{msg.capitalize()} invalida! Informe um valor entre {min} e {max}: ')
		if isinstance(tipo, int):
			valor = int(valor)
		else:
			valor = float(valor)
	return valor

idade = int(input('Informe sua idade: '))
idade = verificador(idade, 1, 150, 'idade')

peso = float(input('Informe seu peso: '))
pseo = verificador(peso, 1, 1000, 'peso')

horas_sono = float(input('Informe quantas horas de sono voce teve nas ultimas 24h: '))
horas_sono = verificador(horas_sono, 0, 24, 'horas de sono')

bo_idade = idade>=16 and idade<=69
bo_peso = peso>50
bo_horas_sono = horas_sono>=6

if bo_idade and bo_peso and bo_horas_sono:
	print('\nVoce pode doar sangue')
else:
	print('\nVoce nao pode ser doador')
	if not bo_idade:
		print(f'Idade ({idade}) fora do intervalo [16, 69] anos')
	if not bo_peso:
		print(f'Peso ({peso:.2f}) abaixo dos 51Kg')
	if not bo_horas_sono:
		print(f'Horas de sono ({horas_sono:.1f}) abaixo das 6h')

"""
3. Considere uma equação do segundo grau f (x) = a · x2 + b · x + c. A partir dos
coeficientes, determine se a equação possui duas raízes reais, uma, ou se não possui.
Dica: ∆ = b2 − 4 · a · c : se delta é maior que 0, possui duas raízes reais;
se delta é 0, possui uma raiz; caso delta seja menor que 0, não possui raiz real
"""
print('\nq3')
print('Solucionar uma eq de grau 2: ax\u00b2 + bx + c')
a = float(input('Informe o valor de \"a\": '))
while a == 0:
	a = float(input('Valor de \"a\" invalido!. Informe um valor nao nulo: '))
b = float(input('Informe o valor de \"b\": '))
c = float(input('Informe o valor de \"c\": '))

delta = b**2 - 4*a*c

if delta == 0:
	n = 1
	x1 = x2 = -b/(2*a)
	str_raiz = 'raiz real'
else:
	n = 2
	if delta > 0:
		x1 = (-b+sqrt(delta))/(2*a)
		x2 = (-b-sqrt(delta))/(2*a)
		str_raiz = 'raizes reais'
	else:
		x1 = f'{-b/(2*a)} + {sqrt(-delta)/(2*a)}i'
		x2 = f'{-b/(2*a)} - {sqrt(-delta)/(2*a)}i'
		str_raiz = 'raizes complexas'

print(f'\nA equacao {a}x\u00b2 {("+" if b>0 else "") + str(b)}x {("+" if c>0 else "") + str(c)} possui {n} {str_raiz}.')
print(f'x1 = {x1}, x2 = {x2}')

"""
4. Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este 
deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual
a 20, este deverá ser apresentado subtraindo-se 5.
"""
print('\nq4.')
num_1 = float(input('Informe o primeiro numero: '))
num_2 = float(input('Informe o segundo numero: '))
soma = num_1 + num_2
if soma > 20:
	soma += 8
	print(f'{num_1} + {num_2} + 8 = {soma}')
else:
	soma -= 5
	print(f'{num_1} + {num_2} - 5 = {soma}')

"""
5. Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a
zero e o quadrado do número caso ele seja negativo.
"""
print('\nq5.')
num = float(input('Informe um numero: '))

if num < 0:
	print(f'({num})\u00b2 = {num**2}')
else:
	print(f'sqrt({num}) = {sqrt(num)}')

"""
6. Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário
digite um número fora desse intervalo, deverá aparecer uma mensagem informando que
não existe mês com este número.
"""
print('\nq6.')
mes = int(input('Informe um numero correspondente a um mes (ex: para junho -> 6): '))
mes_dict = {
	1: 'Janeiro',
	2: 'Fevereiro',
	3: 'Marco',
	4: 'Abril',
	5: 'Maio',
	6: 'Junho',
	7: 'Julho',
	8: 'Agosto',
	9: 'Setembro',
	10: 'Outubro',
	11: 'Novembro',
	12: 'Dezembro',
}

while mes<1 or mes>12:
	mes = int(input('Nao existe mes correspondente a esse numero! Informe algum no intervalo de 1 a 12: '))

print(f'Mes correspondente a {mes} = {mes_dict.get(mes)}')

"""
CAPITULO 14
1. Calcule a tabuada do 13.
"""
print('\nCap 14')
print('q1.')
num = 13

print(f'Tabuada do {num}')
for i in range(1, 11):
	print(f'{num} x {i} = {num*i}')

"""
2. Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
"""
def ler_lista(tamanho):
	lista_num = []
	for i in range(tamanho):
		a = int(input(f'Informe o {i+1}\u00ba numero: '))
		lista_num.append(a)
	return lista_num

print('\nq2.')
lista = ler_lista(5)

print('\nlista =', lista)
print(f'Menor valor da lista: {min(lista)}')

"""
3. Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada
de forma crescente ou False caso contrário.
"""
print('\nq3.')
lista = ler_lista(5)
lista_aux = lista[:]
lista_aux.sort()

print('\nLista:',lista)
print(f'Lista ordenada?: {lista==lista_aux}')

"""
4. Exiba em ordem decrescente todos os números de 500 até 10.
"""
print('\nq4.')
print('Exibindo de 500 ate 10 em ordem decrescente')
print(', '.join(str(i) for i in range(500, 9, -1)))

"""
5. Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.
"""
print('\nq5.')
lista = ler_lista(10)
contador = 0
for i in lista:
	if i>10 and i<50:
		contador += 1

print(f'Quantidade de numeros entre 10 e 50 (intervalo aberto): {contador}')

"""
6. Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
a) idade média das mulheres
b) idade média dos homens
c) idade média do grupo
"""
print('\nq6.')
lista = []
for i in range(10):
	pessoa = {}
	print(f'Informe os dados da Pessoa {i+1}')
	idade = int(input('Idade: '))
	while idade<0 or idade>150:
		idade = int(input('Idade invalida! Informe um valor no intervalo [0, 150]: '))
	sexo = input('Sexo (M/F): ')
	sexo = sexo.upper()
	while sexo != 'M' and sexo != 'F':
		sexo = input('Sexo invalido. Informe ou M ou F: ')
		sexo = sexo.upper()
		print(sexo)
	print()
	pessoa['id'] = f'Pessoa {i+1}'
	pessoa['idade'] = idade
	pessoa['sexo'] = sexo
	lista.append(pessoa)

mulheres = [x for x in lista if 'F' == x.get('sexo')]
homens = [x for x in lista if 'M' == x.get('sexo')]
media_mulheres = sum(m.get("idade") for m in mulheres)/len(mulheres) if len(mulheres)>0 else None
media_homens = sum(h.get("idade") for h in homens)/len(homens) if len(homens)>0 else None

print('mulheres = ', mulheres)
print('homens = ', homens)
print('\na.')
print(f'Idade media das mulheres: {media_mulheres}')

print('\nb.')
print(f'Idade media dos homens: {media_homens}')

print('\nc.')
print(f'Idade media do grupo: {sum(e.get("idade") for e in lista) / len(lista)}')

"""
7. Calcule o somatório dos números de 1 a 100 e imprima o resultado.
"""
print('\nq7.')
n = 100
soma = 0
for i in range(1, n+1):
	soma += i
print(f'Soma dos numeros de 1 a 100: {soma}')
