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

A = | A11  A12 |     B = | B11  B12 |
    | A21  A22 |         | B21  B22 |

🔹 Etapa 2: Cálculo das matrizes S₁ a S₁₀
Criar 10 matrizes auxiliares, cada uma de dimensão n/2 × n/2, por meio de somas ou subtrações das submatrizes:

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

C11 = P5 + P4 - P2 + P6 
C12 = P1 + P2 
C21 = P3 + P4 
C22 = P5 + P1 - P3 - P7

✅ A combinação é feita em tempo Θ(n²)

📊 Definição com Teorema Mestre

....


Este trabalho da disciplina **Algoritmos e Estrutura de Dados II** foi desenvolvido por:

- Andrew Matheus
- Juliana Campos
- Mateus
- Pedro Grangeiro
- Sidney 

## Repositório no GitHub
[🔗 Acesse aqui o repositório](https://github.com/AndrewMBarros/Algoritmos-e-Estruturas-de-Dados-2/tree/main/Algoritmo%20de%20Strassen)



