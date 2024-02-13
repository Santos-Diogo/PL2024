import sys

""" Proibido usar o módulo CSV;
    Ler o dataset, processá-lo e criar os seguintes resultados:
        Lista ordenada alfabeticamente das modalidades desportivas;
        Percentagens de atletas aptos e inaptos para a prática desportiva;
        Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ... """

def main ():
    modalidades= set()
    escaloes= {}
    aptos= 0;
    todos= 0;
    
    header= sys.stdin.readline()
    for line in sys.stdin:
        tokens= line.split(",")

        i= 0
        for token in tokens:
            if (i== 5):
                idade = token
            elif (i== 8):
                modalidades.add(token)
            elif (i== 12):
                if (token):
                    aptos+= 1

            todos+= 1
            i+= 1

    print (modalidades.sort())
    percentagem= aptos/ todos* 100
    print (percentagem)
    print (escaloes)

""" Escaloes ainda nao esta feito """
        
main()