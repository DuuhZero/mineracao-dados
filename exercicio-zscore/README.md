# Lista de Exercícios em Python — Z-Score

Este projeto contém as resoluções em Python da lista de exercícios sobre
Z-Score. Cada exercício está em um arquivo `.py` separado e pode ser
executado de forma independente.

## Como usar

1. (Opcional, mas recomendado) crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute qualquer exercício:
   ```bash
   python exercicio1.py
   ```

## Orientações gerais da lista

- Os exercícios trabalham ideias diferentes do Z-Score, sem exigir programas complexos.
- NumPy e Pandas são usados apenas quando o exercício solicita.
- O cálculo do Z-Score sozinho não encerra a análise — todo exercício traz uma interpretação em linguagem natural.
- `|Z| > 3` é usado apenas como regra prática para indicar valores que merecem investigação.
- Um possível outlier **não** deve ser removido automaticamente.

## Exercícios

### `exercicio1.py` — Distância em passos de desvio-padrão
Calcula a distância entre um valor (115) e a média (100), converte essa
distância em número de desvios-padrão (Z-Score) e imprime uma frase
interpretando o resultado.

### `exercicio2.py` — Acima ou abaixo da média?
Calcula o Z-Score de três valores (`85, 100, 120`) e informa, para cada
um, se está abaixo, exatamente na média ou acima da média, explicando o
significado do sinal do Z-Score (positivo, negativo ou zero).

### `exercicio3.py` — Qual leitura é mais incomum?
Calcula o Z-Score de cinco temperaturas e identifica qual delas está
mais distante da média, comparando os valores absolutos de Z.

### `exercicio4.py` — Latência de uma API
Usa **NumPy** para calcular média e desvio-padrão de um conjunto de
latências, calcula o Z-Score apenas da leitura de 180 ms e verifica se
ela ultrapassa o limite de `|Z| > 3`, reforçando que investigar não
significa apagar o dado automaticamente.

### `exercicio5.py` — Monitoramento de CPU com classificação
Usa **NumPy** para calcular média e desvio-padrão de leituras de CPU,
percorre cada leitura calculando seu Z-Score e classifica o resultado
como `Comum` ou `Investigar`, exibindo no formato
`valor -> Z-Score -> classificação`.

### `exercicio6.py` — O mesmo valor em dois contextos
Compara o Z-Score do mesmo valor (110) em dois grupos com médias iguais
mas desvios-padrão diferentes, explicando por que a mesma distância
absoluta pode ser incomum em um grupo e comum em outro.

### `exercicio7.py` — Função de interpretação
Implementa a função `interpretar_z(z)`, que classifica um Z-Score em
`Investigar` (quando `|Z| > 3`), `Abaixo da média`, `Acima da média` ou
`Na média`, e testa a função com uma lista de valores fornecidos.

### `exercicio8.py` — Z-Score em um DataFrame
Usa **Pandas** para calcular o Z-Score da coluna `Requisicoes` em um
DataFrame, cria as colunas `Z_Score` e `Status` (`Comum`/`Investigar`) e
exibe apenas as linhas marcadas para investigação.

### `exercicio9.py` — Comparação entre IQR e Z-Score
Usa **NumPy** para calcular Q1, Q3, IQR e os limites do IQR, além da
média, desvio-padrão e Z-Score do valor 30 em um conjunto de dados,
comparando o que cada técnica indica sobre esse valor e concluindo que
métodos diferentes podem enxergar o mesmo dado de formas diferentes.

### `exercicio10.py` — Mini análise de eventos de segurança
Usa **Pandas** para calcular o Z-Score de tentativas de login por
evento de segurança, identifica eventos com `|Z| > 3` e reflete sobre
por que um evento estatisticamente incomum pode ser o dado mais
importante de uma análise de segurança.

## Observação sobre desvio-padrão

Nos exercícios que usam **NumPy** (`np.std`), o desvio-padrão é
calculado com `ddof=0` (populacional). Nos exercícios que usam **Pandas**
(`.std()` em uma coluna de DataFrame), o cálculo usa `ddof=1` (amostral),
que é o padrão da biblioteca. Essa é uma diferença comum entre as duas
bibliotecas e não afeta a lógica de interpretação dos exercícios.
