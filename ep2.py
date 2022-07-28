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
while facil < 3 and numero <= 3:
    questao_sorteada = funcoes.sorteia_questao(base, 'facil')
    inedito = funcoes.sorteia_questao_inedida(base, 'facil', listafacil)
    pergunta = funcoes.questao_para_texto(inedito, numero)
    print(pergunta)
    resposta = (input('resposta: '))

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
        print(f'Voce acertou!! Seu premio atual e de R$ {pontuacao}')
        enter = input('Aperte ENTER para continuar...')
        if enter == '':
            print('')
    facil += 1
    numero += 1
if facil == 3:
    print('Ebaa, voce passou para proximo nivel. |MEDIO|')



