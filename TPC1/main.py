import sys

""" Proibido usar o módulo CSV;
    Ler o dataset, processá-lo e criar os seguintes resultados:
        Lista ordenada alfabeticamente das modalidades desportivas;
        Percentagens de atletas aptos e inaptos para a prática desportiva;
        Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ... """

def setEscalao (escaloes, idade):
    range= idade- (idade % 5)
    if range not in escaloes:
        escaloes[range]= 0
    escaloes[range]+= 1

def main ():
    modalidades= set()
    escaloes= {}
    aptos= 0;
    todos= 0;
    
    header= sys.stdin.readline()
    for line in sys.stdin:
        tokens= line.split(",")
        todos+= 1   

        i= 0
        for token in tokens:
            if (i== 5):
                setEscalao (escaloes, int(token)) 
            elif (i== 8):
                modalidades.add(token)
            elif (i== 12):
                if (token== 'true'):
                    print (token)
                    aptos+= 1
            i+=1

    modalidadesL= list(modalidades)
    modalidadesL.sort()
    print ("\nModalidades")
    print (modalidadesL)
    print ("\nPorcentagem de atletas aptos:")
    porcentagem= aptos/ todos* 100
    print (porcentagem)
    print ("\nDistribuicao por escaloes:")
    print (escaloes)

main()
