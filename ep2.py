import random 
import funcoes
import perguntas
from perguntas import quest 

base = funcoes.transforma_base(quest)
print(base)

validar = funcoes.valida_questoes(base['facil'])
print(validar)


print(questao_sorteada)

jogando = True 
while jogando:


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
    facil = 3

    rodajogo = True 
    while rodajogo:

        while facil >= 0:

            questao_sorteada = funcoes.sorteia_questao(base, 'facil')

            if 



        print(base)
