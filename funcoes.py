# IMPORTS
import math
import random 

# TRANSFORMA BASE
def transforma_base(lista):
    i = 0 
    nd = {}
    while i < len(lista):
        questao = lista[i]
        nivel = questao['nivel']
        if nivel not in nd.keys():
            nd[ nivel ] = []
        nd[ nivel ].append(questao)
        i += 1
    return nd 


# VALIDA QUESTAO
def valida_questao(questao):
    problemas = {}
    for chave in ['titulo', 'nivel', 'opcoes', 'correta']:
        if chave not in questao.keys():
            problemas[chave] = 'nao_encontrado'
    if len(questao.keys()) != 4:
        problemas['outro'] = 'numero_chaves_invalido'
    if 'titulo' in questao.keys() and len(questao[ 'titulo'].strip()) == 0:
        problemas['titulo'] = 'vazio'
    if 'nivel' in questao.keys() and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        problemas['nivel'] = 'valor_errado'
    if 'opcoes' in questao.keys():
        if len(questao['opcoes']) != 4:
            problemas['opcoes'] = 'tamanho_invalido'
        else:
            for letra in ['A', 'B', 'C', 'D']:
                if letra not in questao['opcoes'].keys():
                    problemas['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        if 'opcoes' not in problemas.keys():
            opcoes = {}
            for alternativa, resposta in questao['opcoes'].items():
                if len(str(resposta).strip()) == 0:
                    opcoes[alternativa] = 'vazia'
            if len(opcoes) > 0:
                problemas['opcoes'] = opcoes
    if 'correta' in questao.keys():
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            problemas['correta'] = 'valor_errado'
    return problemas


# VALIDA QUESTOES
def valida_questoes(questoes):
    i = 0 
    resposta = []
    while i < len(questoes):
        questao = questoes[i]
        confirmado = valida_questao(questao)
        resposta.append(confirmado)
        i += 1
    return resposta


# SORTEIA QUESTOES
def sorteia_questao(questoes, nivel):
    sorteia = random.choice(questoes[nivel])
    return sorteia


# QUESTAO PARA TEXTO
def questao_para_texto(questao, numero):
    divisoria = '----------------------------------------'
    NUMERO = (f'QUESTAO {numero}')
    TITULO = questao['titulo']
    TXT = divisoria + '\n' + NUMERO + '\n\n' + TITULO + '\n\n' + 'RESPOSTAS:' + '\n'
    for alternativas, op in questao['opcoes'].items():
        TXT += f'{alternativas}: {op}' + '\n'
    return TXT



def sorteia_questao_inedida(dic, nivel, lista):
    while True:
        quest = sorteia_questao(dic, nivel)
        if quest not in lista:
            lista.append(quest)
            return quest