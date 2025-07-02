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