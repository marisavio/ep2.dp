import random 
import funcoes
import perguntas
from perguntas import quest 

base = funcoes.transforma_base(quest)
print(base)

validar = funcoes.valida_questoes(base['facil'])
print(validar)





print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')

nome = input('Qual seu nome? \n')

print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!\nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
enter = input('Aperte ENTER para continuar...')
if enter == '':
    print('\nO jogo já vai começar! Lá vem a primeira questão!\n\nVamos começar com questões do nível FACIL!')
enter = input('Aperte ENTER para continuar...')
if enter == '':
    print('')


    pulo = 3
    ajuda = 2
    dinheiro = 0 
    facil = 0

numero = 1
pontuacao = 0
while facil < 3 and numero <= 3:
    questao_sorteada = funcoes.sorteia_questao(base, 'facil')
    pergunta = funcoes.questao_para_texto(questao_sorteada, numero)
    print(pergunta)
    resposta = (input('resposta: '))
    if resposta != questao_sorteada['correta']:
        break
    else:
        if numero == 1:
            pontuacao = 1000
        print(f'Voce acertou!! Seu premio atual e de R$ {pontuacao}')
    facil += 1
    numero += 1


