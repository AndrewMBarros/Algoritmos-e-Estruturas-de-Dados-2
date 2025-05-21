#Algoritmo de Strassen para multiplicação de matrizes

Este repositório contém uma explicação teórica, implementação e análise de complexidade do Algoritmo de Strassen, um algoritmo eficiente para multiplicação de matrizes quadradas.

- ✅ Teoria do algoritmo
- ✅ Implementação e tempo de execução
- ✅ Teorema Mestre para complexidade

📘 Teoria

- O algoritmo de Strassen é um método recursivo para multiplicação de matrizes que reduz o número de multiplicações necessárias. Ele divide o problema em subproblemas menores, e realiza apenas 7 multiplicações (em vez de 8), o que reduz a complexidade assintótica.
- Segundo o livro Algoritmos: Teoria e Prática de Cormen, o algoritmo pode ser dividido em quatro etapas:


🔹 Etapa 1: Divisão das matrizes
Dividir as matrizes de entrada A e B em 4 submatrizes cada, de tamanho n/2 × n/2:

```text
A = | A11  A12 |     B = | B11  B12 |
    | A21  A22 |         | B21  B22 |
```

🔹 Etapa 2: Cálculo das matrizes S₁ a S₁₀
Criar 10 matrizes auxiliares, cada uma de dimensão n/2 × n/2, por meio de somas ou subtrações das submatrizes:

```text
S1  = B12 - B22 
S2  = A11 + A12 
S3  = A21 + A22 
S4  = B21 - B11 
S5  = A11 + A22 
S6  = B11 + B22 
S7  = A12 - A22 
S8  = B21 + B22 
S9  = A11 - A21 
S10 = B11 + B12
```
Podemos criar todas as 10 matrizes no tempo Θ(n²).

🔹 Etapa 3: Cálculo dos produtos P₁ a P₇

Usando as submatrizes e as matrizes S₁ a S₁₀, calcula-se 7 multiplicações recursivas:

P1 = A11 × S1 
P2 = S2  × B22 
P3 = S3  × B11 
P4 = A22 × S4 
P5 = S5  × S6 
P6 = S7  × S8 
P7 = S9  × S10

✅ Cada multiplicação ocorre sobre matrizes de dimensão n/2 × n/2

🔹 Etapa 4: Cálculo da matriz resultado:

As submatrizes da matriz C resultado são combinadas da seguinte forma:

```text
C11 = P5 + P4 - P2 + P6 
C12 = P1 + P2 
C21 = P3 + P4 
C22 = P5 + P1 - P3 - P7
```
✅ A combinação é feita em tempo Θ(n²)

---

📊 Definição com Teorema Mestre

O Teorema Mestre define que, se temos uma recorrência da forma:

    T(n) = a * T(n / b) + f(n)

onde:

- a ≥ 1  
- b > 1  
- f(n) é uma função não negativa

Temos três casos:

1. Se f(n) < n^log_b(a), então:  
       T(n) = Θ(n^log_b(a))

2. Se f(n) = n^log_b(a), então:  
       T(n) = Θ(f(n) * log n)

3. Se f(n) > n^log_b(a), então:  
       T(n) = Θ(f(n))
---

🧠 Aplicação – Teorema Mestre no Algoritmo

No código, as funções de soma de matrizes, criação das matrizes A e B e o cálculo das 4 submatrizes possuem complexidade:

    f(n) = n²

As multiplicações de matrizes (P1...P7) dividem as matrizes de entrada em submatrizes de tamanho n/2. Como realizamos 7 chamadas recursivas, temos:

    T(n) = 7 * T(n / 2) + n²

Agora aplicamos o Teorema Mestre:

- a = 7  
- b = 2  
- f(n) = n²  
- log_b(a) = log₂(7) ≈ 2.81

Como:

    n² < n^2.81

Estamos no **caso 1** do Teorema Mestre, portanto:

    T(n) = Θ(n^log₂7) ≈ Θ(n^2.81)


✅ **Conclusão**:  
A complexidade do algoritmo é **O(n^2.81)**, o que é mais eficiente que a multiplicação tradicional de matrizes, que possui complexidade **O(n³)**.


<br>

---
Este trabalho da disciplina **Algoritmos e Estrutura de Dados II** foi desenvolvido por:

- Andrew Matheus
- Juliana Campos
- Mateus Henrique Freitas
- Pedro Grangeiro
- Sidney Sant'Anna

## Repositório no GitHub
[🔗 Acesse aqui o repositório](https://github.com/AndrewMBarros/Algoritmos-e-Estruturas-de-Dados-2/tree/main/Algoritmo%20de%20Strassen)
