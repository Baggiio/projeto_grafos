# imprime as boas-vindas ao usuário
print("Seja bem-vindo ao algoritmo de análise de grafos!")

# imprime o nome e numero dos elementos do grupo
print("Algoritmo desenvolvido por:")
print("Gustavo Garcia Bagio - RA: 24.122.012-8")
print("Cauan Vinicius Espinha de Sousa - RA: 24.122.089-6")

# cria a função que será utilizada para "colorir" o grafo e verificar se é bipartido
def colorir_grafo(A, cor, posicao, v):
    if cor[posicao] != -1 and cor[posicao] != v:
        return False
    cor[posicao] = v
    resposta = True
    for i in range(len(A)):
        if A[posicao][i]:
            if cor[i] == -1:
                resposta &= colorir_grafo(A, cor, i, 1-v)   
            if cor[i] !=-1 and cor[i] != 1-v:
                return False
        if not resposta:
            return False
    global color
    color = cor
    return True

# realiza a leitura da matriz de adjacência do grafo e armazena em uma lista
A = []
file = open("A.txt", "r")
lines = file.readlines()
try:
    for each in lines:
        A.append(list(int(x) for x in each.strip("\n").split(" ")))
except:
    print("\nMatriz inválida! Verifique se há espaços adicionais no arquivo texto.")
    exit()
    

# imprime a matriz de adjacencia do grafo
print("\nMatriz de adjacencia do grafo:\n")
print("%5s" % "", end="")
for i in range(len(A)):
    print("%5s" % ("v" + str(i+1))) if i == (len(A)-1) else print("%5s" % ("v" + str(i+1)), end="")
for i in range(len(A)):
    for j in range(len(A[0])):
        if j == 0: print("%5s" % ("v" + str(i+1)), end="")
        print("%5d" % (A[i][j])) if j == (len(A[0])-1) else print("%5d" % (A[i][j]), end="")

print()

# verifica se o grafo é simples ou complexo
complexo = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            if A[i][j] > 0:
                complexo = 1
        else:
            if A[i][j] > 1:
                complexo = 1

# caso o grafo seja complexo, imprime as arestas duplas e laços
if complexo == 1:
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
    print("O grafo é complexo, pois há arestas múltiplas ou laços:")
    if arestas_multiplas:
        for i in range(len(arestas_multiplas)):
            print("\tOcorrem %d arestas múltiplas entre v%d e v%d." % (arestas_multiplas[i][0], arestas_multiplas[i][1], arestas_multiplas[i][2]))
    if lacos:
        print("\tOcorre %d laço em v%d." % (lacos[0][0], lacos[0][1])) if len(lacos) == 1 else print("Ocorrem %d laços em v%d." % (lacos[i][0], lacos[i][1]))
else:
    print("O grafo é simples, pois não possui arestas múltiplas ou laços.")

print()

# verifica o grau de cada vértice e imprime a sequência de graus do grafo
graus = []
for i in range(len(A)):
    if A[i][i] > 0:
        graus.append(sum(A[i]) + A[i][i])
    else:
        graus.append(sum(A[i]))
graus.sort(reverse=True)
print("Sequência de graus: ", end=""); print(*graus, sep=", ", end=".\n")

print()

# conta o número de arestas do grafo e imprime
arestas = 0
for i in range(len(A)):
    if A[i][i] > 0:
        arestas += (sum(A[i]) + A[i][i])
    else:
        arestas += sum(A[i])
print("O grafo possui %d arestas." % (arestas/2))

print()

# verifica se o grafo é completo ou não
if complexo == 0:
    completo = 1
    for i in range(len(A)):
        if completo == 1:
            for j in range(len(A[i])):
                if i == j:
                    pass
                else:
                    if A[i][j] == 0:
                        print("O grafo não é completo, pois não possui aresta entre v%d e v%d." % (i+1, j+1))
                        completo = 0
                        break
        else:
            break
    if completo == 1:
        print("O grafo é completo.")
else:
    print("O grafo não pode ser completo, pois é complexo.")

print()

# verifica se o grafo é regular ou não
if graus[0] == graus[-1]:
    print("O grafo é regular, pois todos os vértices possuem grau %d." % graus[0])
else:
    print("O grafo não é regular, pois os vértices possuem graus diferentes.")

print()

# verifica se o grafo é bipartido ou não, caso seja, imprime a bipartição
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

    # verifica se o grafo bipartido é bipartido completo
    if complexo == 0:
        x1 = []
        y1 = []
        for i in range(len(color)):
            if color[i] == 0:
                x1.append(i)
            else:
                y1.append(i)
        found = 0
        for i in range(len(x1)):
            if found == 0:
                for j in range(len(y)):
                    if A[x1[i]][y1[j]] == 0:
                        print("\tO grafo não é bipartido completo, pois v%d não é adjacente a v%d." % (x1[i]+1, y1[j]+1))
                        found = 1
                        break
            else:
                break
        if found == 0:
            print("\tO grafo é bipartido completo, pois cada vértice de x está associado com cada vértice de y.")
            print("\tO grafo pode ser denotado como K%s,%s." % (str(len(x)), str(len(y))))
    else:
        print("\tO grafo não pode ser bipartido completo pois é complexo.")
else:
    print("O grafo não é bipartido, pois não é possível separar seus vértices em dois subconjuntos x e y tal que toda aresta do grafo une um vértice de x a outro de y.")

print()

# solicita uma entrada do usuario para encerrar o programa
print("Pressione qualquer tecla para sair...")
input()
