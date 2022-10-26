def cripto(frase):

# Declaração de matriz
    linhas=3
    vazios=1
    for lin in range(0,linhas):
        vazios=vazios+lin
    colunas=int(round((len(frase)+vazios)/linhas))
    matriz=[]
    mLinhas=[]
    for c in range(0,colunas):
        mLinhas.append("_")
    for l in range(0,linhas):
        matriz.append(mLinhas.copy())
#Criptografia
    cont=0
    for c in range(0,colunas):
        for l in range(0,linhas):
            idxColuna = (c+l) % colunas
            if cont < len(frase):
                letra=frase[cont]
                matriz[l][idxColuna]=letra
                cont += 1

    fraseCripto=[]
    for l in range(0,linhas):
        for c in range (0,colunas):
            fraseCripto.append(matriz[l][c])
    fraseCripto="".join(fraseCripto)
    fraseCripto=fraseCripto.replace(' ','_')

    return fraseCripto

#Descriptografia

def desCripto(fraseCripto):
    linhas=3
    colunas = int(len(fraseCripto)/ linhas)
    matriz = []
    mLinhas = []
    #Declaração da Matriz
    for c in range (0,colunas):
        mLinhas.append("_")
    for l in range(0,linhas):
        matriz.append(mLinhas.copy())

    #Descriptografia
    cont=0
    for l in range(0, linhas):
        for c in range(0,colunas):
            if cont < len(fraseCripto):
                letra=fraseCripto[cont]
                matriz[l][c]=letra
                cont+=1

    fraseDescripto=[]
    for c in range(0,colunas):
        for l in range(0,linhas):
            idxColuna=(c+l) % colunas
            letra=matriz[l][idxColuna]
            fraseDescripto.append(letra)
    fraseDescripto="".join(fraseDescripto)
    fraseDescripto=fraseDescripto.replace("_"," ").strip()

    return fraseDescripto

criptografar=cripto("ANDRE CARCIANO AMERICO DE MATOS")
descriptografar=desCripto(criptografar)
print(f"A frase criptografada é: {criptografar}")
print(f"A frase descriptografada é: {descriptografar}")












