### JOGO DA VELHA DE TERMINAL ### Marcelo
import random
def bot_turn(matriz):

	return (random.choice(range(1, 10)))

def atualizar(matriz):
	aux = ''
	for i in range(3):
		for i2 in range(3):
			aux += matriz[i][i2]
			if i2 != 2:
				aux += ' | '
		print('   '+ aux)
		aux = ''
		if i != 2:
			print('   ' + '---------')
			
	print('-----------------')

def inserir(matriz, x, y, oque):
	matriz[x][y] = oque

def ganhou(matriz, e):
	ganhou = False
	dic = {'1': [], '2':[], '3': []}
	for ii in range(3):
		for jj in range(3):
			if matriz[ii][jj] == e:
				dic[str(ii + 1)].append(jj + 1)

	for elemento in dic:
		if len(dic[elemento]) == 3:
			return True
	for i in range(1, 4):
		if i in dic['1'] and i in dic['2'] and i in dic['3']:
			return True
	if 1 in dic['1'] and 2 in dic['2'] and 3 in dic['3']:
		return True
	if 3 in dic['1'] and 2 in dic['2'] and 1 in dic['3']:
		return True
	
	return False

versusbot = input('Deseja jogar contra o computador?(y/n):  ')
if versusbot == 'y': versusbot = True
else: versusbot = False

matriz = [[' ', ' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]
atualizar(matriz)
vez = 'X'
colocados = 0
while True:

	if vez == 'X':
		print('Vez do jogador X')
	elif not versusbot:
		print('Vez do jogador O')
	else:
		print('O computador realizou sua jogada!')

	while True:
		if vez == 'X' or (vez == 'O' and not versusbot):
			try:
				x = int(input('Insira a casa de 1 a 9: '))
			except:
				print('Tente inserir um número de 1 a 9 !!!')
				continue
		elif vez == 'O':
			x = bot_turn(matriz)
		if x < 4 and x > 0:
			y = 1
		elif x > 3 and x < 7:
			x -= 3
			y = 2
		elif x > 6 and x < 10:
			x -= 6
			y = 3
		else:
			print('\nInsira coordenadas válidas')
			print('Tente novamente\nVez do jogador ' + vez)
			continue
		x, y = y, x
		if matriz[x - 1][y - 1] == ' ':
			if vez == 'X':
				inserir(matriz, x - 1, y - 1, 'X')
				colocados += 1
				break
			else:
				inserir(matriz,x - 1, y - 1, 'O')
				colocados += 1
				break
		else:
			if vez == 'X' or not versusbot:
				print('Posição já ocupada ou inexistente.')
				print('Tente novamente\n')
				print('Vez do jogador ' + vez)

	atualizar(matriz)

	if ganhou(matriz, vez):
		if versusbot:
			vez = 'O COMPUTADOR'
		print(vez + ' GANHOU!')
		break
	
	if colocados == 9:
		print('EMPATE')
		break
	
	if vez == 'X':
		vez = 'O'
	else:
		vez = 'X'
