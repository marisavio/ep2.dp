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
numero = 1
pontuacao = 0
listafacil = []
questoes = 1
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

    # QUESTÕES FACEIS 
    if questoes <= 3:
        questao_sorteada = funcoes.sorteia_questao(base, 'facil')
        inedito = funcoes.sorteia_questao_inedida(base, 'facil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('Qual sua resposta?! '))
    # PASSANDO PARA O NIVEL MEDIO 
    if questoes == 4:
        print('HEY! Você passou para o nível MEDIO!')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')
    # QUESTÕES MÉDIAS 
    if questoes > 3 and questoes <= 6:
        questao_sorteada = funcoes.sorteia_questao(base, 'medio')
        inedito = funcoes.sorteia_questao_inedida(base, 'medio', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('Qual sua resposta?! '))
    # PASSANDO PARA O NIVEL DIFICIL 
    if questoes == 7:
        print('HEY! Você passou para o nível DIFICIL!')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')
    # QUESTÕES DIFICEIS 
    if questoes > 6 and questoes <= 9:
        questao_sorteada = funcoes.sorteia_questao(base, 'dificil')
        inedito = funcoes.sorteia_questao_inedida(base, 'dificil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('Qual sua resposta?!  \n'))

    # PULOS
    if resposta == 'pular' and pulo > 0:
        pulo -= 1
        pula_pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pula_pergunta)
        print('')

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
        resposta = (input('Qual sua resposta?! '))
        # USO DE UMA AJUDA POR QUESTÃO
        if tentativa == 0:
            print('Voce nao tem direito a mais ajuda(s). Responda a pergunta: ')
            enter = input('Aperte ENTER para continuar...')
            if enter == '':
                print('')
            print(pergunta)
            resposta = (input('Qual sua resposta?! '))



    if resposta == inedito['correta']:
        # PONTUAÇÃO A CADA QUESTÃO 
        if numero == 1:
            pontuacao = 1000
        elif numero == 2:
            pontuacao = 5000
        elif numero == 3:
            pontuacao = 10000
        elif numero == 4:
            pontuacao = 30000
        elif numero == 5:
            pontuacao = 50000
        elif numero == 6:
            pontuacao = 100000
        elif numero == 7:
            pontuacao = 300000
        elif numero == 8:
            pontuacao = 500000
        elif numero == 9:
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
    questoes += 1
    numero += 1
