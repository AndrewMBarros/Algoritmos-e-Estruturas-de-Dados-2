import time
def min_palindrome_cuts(s):
    n = len(s)
    if n == 0:
        return 0, []

    #Marca início do tempo de pré-processamento
    t0 = time.time()
    #Tabela para marcar se s[i..j] é palíndromo
    is_palin = [[False] * n for _ in range(n)]

    #O(n)
    for i in range(n):
        is_palin[i][i] = True

    #O(n)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palin[i][i + 1] = True

    #O(n²)
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palin[i + 1][j - 1]:
                is_palin[i][j] = True

    t1 = time.time()
    #Tempo de pré-processamento
    preproc_time = t1 - t0

    # Marca início do tempo de DP
    t2 = time.time()

cuts = [0] * n
    path = [[] for _ in range(n)]  # guarda partições

    #O(n²)
    for i in range(n):
      #verifica se s[0...i] é um palindromo
        if is_palin[0][i]:
            cuts[i] = 0
            path[i] = [s[0:i+1]]
        else:

            #maior numero de cortes
            cuts[i] = i

            #verifica se s[1...i] tem algum corte melhor
            for j in range(1, i + 1):
                if is_palin[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    # 0 1 2 ... j-1 | j ... i
                    cuts[i] = cuts[j - 1] + 1
                    path[i] = path[j - 1] + [s[j:i + 1]]

    t3 = time.time()
    dp_time = t3 - t2
    total_time = t3 - t0

    return cuts[-1], path[-1], preproc_time, dp_time, total_time

exemplos = ["aab", "geek", "noon", "banana"]
    
def exemplos():
    for palavra in exemplos:
        cortes, partes, preproc, dp, total = min_palindrome_cuts(palavra)
        print(f"\nPalavra: '{palavra}'")
        print(f"  Cortes mínimos: {cortes}")
        print(f"  Palíndromos: {' | '.join(partes)}")
        print(f"  Tempo pré-processamento (s): {preproc:.6f}")
        print(f"  Tempo DP (s): {dp:.6f}")
        print(f"  Tempo Total (s): {total:.6f}")
