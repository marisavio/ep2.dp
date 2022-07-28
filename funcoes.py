import random 

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

def valida_questoes(questao):

    confirmado = valida_questao(questao)

    minhalista = confirmado.items()
    minhalista = list(minhalista)
    return minhalista

def sorteia_questao(questoes, nivel):
    sorteia = random.choice(questoes[nivel])
    return sorteia

