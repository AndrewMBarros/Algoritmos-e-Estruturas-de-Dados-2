# 🔁 Grupo 8 - Número Máximo de Palavras Palíndromas em Texto

## 🧩 Descrição do Problema

Dada uma string, particioná-la em substrings de forma que cada uma seja um palíndromo (lê-se igual de frente para trás e vice-versa), minimizando o número de cortes necessários.
Um **palíndromo** é uma palavra ou frase que se lê da mesma forma de trás para frente (ex: "ana", "radar", "noon").

---

## 🚀 Funcionalidade

O algoritmo implementado realiza:

* **Pré-processamento:** Geração de uma tabela que marca todas as substrings palíndromas.
* **Programação Dinâmica (DP):** Cálculo do número mínimo de cortes necessários para dividir a string em palíndromos.
* **Medição de desempenho:** Tempo gasto em cada fase (pré-processamento, DP e total).
* **Exemplos de execução com saída formatada.**

---

## 🧠 Complexidade do Algoritmo

## 📈 Análise de Complexidade (com somas explícitas)

### O algoritmo tem duas fases principais:


###  1️⃣ Construção da Tabela de Palíndromos

- Substrings de tamanho 1: $O(n)$
- Substrings de tamanho 2: $O(n)$
- Substrings de tamanho ≥ 3: $O(n^2)$

 Soma desta fase:
$O(n) + O(n) + O(n^2) = O(n^2)$

<br>

###  2️⃣ Programação Dinâmica (Cálculo dos Cortes)

- Para cada posição $i$, verifica todas as quebras $j$: $O(n^2)$

<br>

###  3️⃣ Complexidade Total do Algoritmo


$O(n^2) + O(n^2) = O(n^2)$


**Resultado Final:**  
**Complexidade Total:** $O(n^2)$


## 📄 Código Principal

```python
import time

def min_palindrome_cuts(s):
    n = len(s)
    if n == 0:
        return 0, []

    # Início do tempo de pré-processamento
    t0 = time.time()

    is_palin = [[False] * n for _ in range(n)]

    for i in range(n):
        is_palin[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palin[i][i + 1] = True

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palin[i + 1][j - 1]:
                is_palin[i][j] = True

    t1 = time.time()
    preproc_time = t1 - t0

    # Início do tempo de programação dinâmica
    t2 = time.time()

    cuts = [0] * n
    path = [[] for _ in range(n)]

    for i in range(n):
        if is_palin[0][i]:
            cuts[i] = 0
            path[i] = [s[0:i+1]]
        else:
            cuts[i] = i
            for j in range(1, i + 1):
                if is_palin[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
                    path[i] = path[j - 1] + [s[j:i + 1]]

    t3 = time.time()
    dp_time = t3 - t2
    total_time = t3 - t0

    return cuts[-1], path[-1], preproc_time, dp_time, total_time
```

---

## 🧪 Exemplos de Execução

```python
exemplos = ["aab", "geek", "noon", "banana"]

def testar_exemplos():
    for palavra in exemplos:
        cortes, partes, preproc, dp, total = min_palindrome_cuts(palavra)
        print(f"\nPalavra: '{palavra}'")
        print(f"  Cortes mínimos: {cortes}")
        print(f"  Palíndromos: {' | '.join(partes)}")
        print(f"  Tempo pré-processamento (s): {preproc:.6f}")
        print(f"  Tempo DP (s): {dp:.6f}")
        print(f"  Tempo Total (s): {total:.6f}")

testar_exemplos()
```

### 📌 Saída Esperada:

```
Palavra: 'aab'
  Cortes mínimos: 1
  Palíndromos: aa | b

Palavra: 'geek'
  Cortes mínimos: 2
  Palíndromos: g | ee | k

Palavra: 'noon'
  Cortes mínimos: 0
  Palíndromos: noon

Palavra: 'banana'
  Cortes mínimos: 1
  Palíndromos: b | anana
```

---

## 👥 Grupo 8
Este trabalho da disciplina **Algoritmos e Estrutura de Dados II** foi desenvolvido por:

- Andrew Matheus
- Juliana Campos
- Mateus Henrique Freitas
- Pedro Grangeiro
- Sidney Sant'Anna

---
