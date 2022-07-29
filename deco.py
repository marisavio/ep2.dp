import random 
import funcoes
import perguntas
from perguntas import quest 

# DESIGN
linha = print('================================================')

# VARIAVEIS
base = funcoes.transforma_base(quest)
pulo = 3
ajuda = 2
facil = 0 
numero = 0
pontuacao = 0
listafacil = []
questoes = 0
tentativa = 1

# INTRO
print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')
nome = input('Qual seu nome? \n')
print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!\nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
enter = input('Aperte ENTER para continuar...')
if enter == '':
    print('\nO jogo já vai começar! Lá vem a primeira questão!\n\nVamos começar com questões do nível FACIL!')
enter = input('Aperte ENTER para continuar...')
if enter == '':
    print('')

# COMEÇANDO O JOGO 
jogando = True 
while jogando:
    # QUESTOES FACEIS
    if questoes <= 3:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'facil')
        inedito = funcoes.sorteia_questao_inedida(base, 'facil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
    # QUESTÕES MÉDIAS 
    if questoes > 3 and questoes <= 6:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'medio')
        inedito = funcoes.sorteia_questao_inedida(base, 'medio', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
    # QUESTÕES DIFICEIS 
    if questoes > 6 and questoes <= 9:
        numero += 1
        questao_sorteada = funcoes.sorteia_questao(base, 'dificil')
        inedito = funcoes.sorteia_questao_inedida(base, 'dificil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)

    # PERGUNTA
    resposta = (input('Qual sua resposta?! '))

    # PULO
    if resposta == 'pular' and pulo >= 1:
        pulo -= 1
        print(f'Voce tem {pulo} pulos.')
        print('')
    if resposta == 'pular' and pulo <= 0:
        print('Voce nao tem mais pulos. Responda a pergunta')
        resposta = (input('Qual sua resposta?! '))
        if resposta == 'pular':
            print('Que pena! Voce errou e vai sair sem nada.')
            break
        
    # AJUDA 
    if resposta == 'ajuda' and tentativa != 0:
        # VARIAVEIS DA AJUDA 
        aleatoria = inedito['opcoes']['A']
        ajudar = funcoes.gera_ajuda(questao_sorteada)
        tentativa -= 1
        # QUANDO NÃO TEM MAIS DIREITO A AJUDA 
        if ajuda < 0:
            print('Não deu! Você não tem mais direito a ajuda!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        # QUANDO TEM DIREITO A UMA AJUDA 
        if ajuda == 1:
            print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(f'DICA:\nOpções certamente erradas:{aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        # QUANDO TEM DIREITO A DOIS PULOS
        if ajuda == 2:
            print('Ok, lá vem ajuda! Você tem direito a mais uma ajuda!')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(f'DICA:\nOpções certamente erradas:{aleatoria}')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
        print(pergunta)
        # USO DE UMA AJUDA POR QUESTÃO
        if tentativa == 0:
            print('Voce nao tem direito a mais ajuda(s). Responda a pergunta: ')
            resposta = (input('Qual sua resposta?! '))
            if resposta == 'ajuda':
                print('Que pena! Voce errou e vai sair sem nada.')
                break

    # ACERTOU
    if resposta == inedito['correta']:
        questoes += 1
        # PONTUAÇÃO A CADA QUESTÃO 
        if questoes == 1:
            pontuacao = 1000
        elif questoes == 2:
            pontuacao = 5000
        elif questoes == 3:
            pontuacao = 10000
            print('HEY! Você passou para o nível MEDIO!')
        elif questoes == 4:
            pontuacao = 30000
        elif questoes == 5:
            pontuacao = 50000
        elif questoes == 6:
            pontuacao = 100000
            print('HEY! Você passou para o nível DIFICIL!')
        elif questoes == 7:
            pontuacao = 300000
        elif questoes == 8:
            pontuacao = 500000
        elif questoes == 9:
            print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais! ')
            pontuacao = 1000000
        print(f'Voce acertou!! Seu premio atual e de R$ {pontuacao}')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')

   
    # QUANDO SE ERRA A RESPOSTA DA QUESTÃO 
    if resposta != 'ajuda' and resposta != inedito['correta'] and resposta != 'pular':
        print('Que pena! Voce errou e vai sair sem nada.')
        break
    ajuda -= 1
    facil += 1