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

        