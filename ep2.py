import random 
import funcoes
import perguntas
from perguntas import quest 


# DESIGN
linha = print('================================================')

# VARIAVEIS
base = funcoes.transforma_base(quest)
validarfacil = funcoes.valida_questoes(base['facil'])
validarmedio = funcoes.valida_questoes(base['medio'])
validardificil = funcoes.valida_questoes(base['dificil'])
pulo = 3
ajuda = 2
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


facil = 0 
numero = 1
pontuacao = 0
listafacil = []
niveis= ['facil', 'medio', 'dificil']
questoes = 1
jogando = True 
while jogando:
    if questoes <= 3:
        questao_sorteada = funcoes.sorteia_questao(base, 'facil')
        inedito = funcoes.sorteia_questao_inedida(base, 'facil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('resposta: '))
    if questoes == 4:
        print('HEY! Você passou para o nível MEDIO!')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')

    if questoes > 3 and questoes <= 6:
        questao_sorteada = funcoes.sorteia_questao(base, 'medio')
        inedito = funcoes.sorteia_questao_inedida(base, 'medio', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('resposta: '))
    if questoes == 7:
        print('HEY! Você passou para o nível DIFICIL!')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')

    if questoes > 6 and questoes <= 9:
        questao_sorteada = funcoes.sorteia_questao(base, 'dificil')
        inedito = funcoes.sorteia_questao_inedida(base, 'dificil', listafacil)
        pergunta = funcoes.questao_para_texto(inedito, numero)
        print(pergunta)
        resposta = (input('Qual sua resposta?!  \n'))
    
    if resposta != inedito['correta']:
        print('Que pena! Voce errou e vai sair sem nada.')
        break
    else:
        if numero == 1:
            pontuacao = 1000
        if numero == 2:
            pontuacao = 5000
        if numero == 3:
            pontuacao = 10000
        if numero == 4:
            pontuacao = 30000
        if numero == 5:
            pontuacao = 50000
        if numero == 6:
            pontuacao = 100000
        if numero == 7:
            pontuacao = 300000
        if numero == 8:
            pontuacao = 500000
        if numero == 9:
            print('PARABÉNS, você zerou o jogo e ganhou um milhão de reais! ')
            pontuacao = 1000000
        print(f'Voce acertou!! Seu premio atual e de R$ {pontuacao}')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')    
        

    facil += 1
    questoes += 1
    numero += 1
    break 





