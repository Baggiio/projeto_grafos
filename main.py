def verificar_complexo(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i == j:
                if A[i][j] > 0:
                    return True
            else:
                if A[i][j] > 1:
                    return True
    return False

def exibir_complexo(A):
    if verificar_complexo(A):
        arestas_multiplas = []
        lacos = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    if A[i][j] > 0:
                        lacos.append([A[i][j], (i+1)])
                elif i - j < 0:
                    if A[i][j] > 1:
                        arestas_multiplas.append([A[i][j], (i+1), (j+1)])
        print("O grafo é complexo:")
        if arestas_multiplas:
            for i in range(len(arestas_multiplas)):
                print("\tOcorrem %d arestas múltiplas entre v%d e v%d." % (arestas_multiplas[i][0], arestas_multiplas[i][1], arestas_multiplas[i][2]))
        if lacos:
            print("\tOcorre %d laço em v%d." % (lacos[0][0], lacos[0][1])) if len(lacos) == 1 else print("Ocorrem %d laços em v%d." % (lacos[i][0], lacos[i][1]))
    else:
        print("O grafo é simples, pois não possui arestas múltiplas ou laços.")

def verificar_graus(A):
    graus = []
    for i in range(len(A)):
        if A[i][i] > 0:
            graus.append(sum(A[i]) + A[i][i])
        else:
            graus.append(sum(A[i]))
    graus.sort(reverse=True)
    print("Sequência de graus: ", end=""); print(*graus, sep=", ", end=".\n")

def numero_arestas(A):
    arestas = 0
    for i in range(len(A)):
        if A[i][i] > 0:
            arestas += (sum(A[i]) + A[i][i])
        else:
            arestas += sum(A[i])
    print("O grafo possui %d arestas." % (arestas/2))

def verificar_completo(A):
    if verificar_complexo(A) == False:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    pass
                else:
                    if A[i][j] == 0:
                        print("O grafo não é completo, pois não possui aresta entre v%d e v%d." % (i+1, j+1))
                        return
        print("O grafo é completo.")
    else:
        print("O grafo não pode ser completo, pois é complexo.")

def verificar_regular(A):
    graus = []
    for i in range(len(A)):
        if A[i][i] > 0:
            graus.append(sum(A[i]) + A[i][i])
        else:
            graus.append(sum(A[i]))
    graus.sort(reverse=True)
    if graus[0] == graus[-1]:
        print("O grafo é regular, pois todos os vértices possuem grau %d." % graus[0])
    else:
        print("O grafo não é regular, pois os vértices possuem graus diferentes.")

def colorir_grafo(A, cor, posicao, v):
    if cor[posicao] != -1 and cor[posicao] != v:
        return False
    cor[posicao] = v
    resp = True
    for i in range(len(A)):
        if A[posicao][i]:
            if cor[i] == -1:
                resp &= colorir_grafo(A, cor, i, 1-v)   
            if cor[i] !=-1 and cor[i] != 1-v:
                return False
        if not resp:
            return False
    global color
    color = cor
    return True

def verificar_bipartido_completo(A, color):
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    if verificar_complexo(A) == False:
        x = []
        y = []
        for i in range(len(color)):
            if color[i] == 0:
                x.append(i)
            else:
                y.append(i)
        for i in range(len(x)):
            for j in range(len(y)):
                if A[x[i]][y[j]] == 0:
                    print("\tO grafo não é bipartido completo, pois v%d não é adjacente a v%d." % (x[i]+1, y[j]+1))
                    return
        print("\tO grafo é bipartido completo: K%s,%s." % (str(len(x)).translate(SUB), str(len(y)).translate(SUB)))
        return
    else:
        print("\tO grafo não pode ser bipartido completo pois é complexo.")
        return
  
def verificar_bipartido(A):
    cor = [-1] * len(A)
    posicao = 0
    if colorir_grafo(A, cor, posicao, 0):
        x = []
        y = []
        for i in range(len(color)):
            if color[i] == 0:
                x.append("v"+str(i+1))
            else:
                y.append("v"+str(i+1))
        print("O grafo é bipartido com bipartição x = {%s} e y = {%s}." % (", ".join(x), ", ".join(y)))
        verificar_bipartido_completo(A, color)
    else:
        print("O grafo não é bipartido.")

def main():
    A = []
    file = open("G.txt", "r");
    lines = file.readlines();
    for each in lines:
        A.append(list(int(x) for x in each.strip("\n").split(" ")));
    
    exibir_complexo(A); print()
    verificar_graus(A); print()
    numero_arestas(A); print()
    verificar_completo(A); print()
    verificar_regular(A); print()
    verificar_bipartido(A); print()
    
if __name__ == "__main__":
    main()
