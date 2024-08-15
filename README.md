# Comparação de Algoritmos de Substituição de Páginas: FIFO vs. Aging

Este projeto implementa e compara dois algoritmos de substituição de páginas: FIFO (First-In, First-Out) e Aging. O objetivo é analisar o desempenho de cada algoritmo em termos de faltas de página para diferentes números de molduras de páginas.

## Equipe

- Rai Ferreira
- Isabelly Pinheiro
- Elias Sombra

## Descrição

O projeto gera uma sequência de referências de páginas aleatórias e calcula o número de faltas de página para os algoritmos FIFO e Aging. Os resultados são apresentados para diferentes números de molduras de páginas, permitindo uma comparação direta entre os algoritmos.

## Estrutura do Projeto

- `fifo(pages, number_of_page_frames)`: Implementa o algoritmo FIFO.
- `aging(pages, number_of_page_frames)`: Implementa o algoritmo Aging.
- `generate_references(num_references, num_pages)`: Gera uma lista de referências de páginas aleatórias.
- `save_references_to_file(references, filename)`: Salva a lista de referências de páginas em um arquivo.
- `compare_algorithms(num_references, num_pages, page_frames_list)`: Compara os algoritmos FIFO e Aging para diferentes números de molduras de páginas.

## Requisitos

- Python 3.x

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script principal:
   ```bash
   python main.py
   ```

3. O script gerará uma sequência de referências de páginas, salvará em um arquivo `references.txt` e imprimirá o número de faltas de página para os algoritmos FIFO e Aging.

## Exemplo de Saída

```
Número de Molduras | Faltas FIFO | Faltas Aging
5                  | 899         | 899
10                 | 798         | 789
25                 | 477         | 510
30                 | 407         | 419
```

## Conclusões

- **Desempenho Similar com Poucas Molduras**: Ambos os algoritmos têm desempenho similar com um número muito limitado de molduras.
- **Melhoria com o Aumento das Molduras**: O número de faltas de página diminui para ambos os algoritmos à medida que o número de molduras aumenta.
- **FIFO vs. Aging**: FIFO teve um desempenho ligeiramente melhor com um número maior de molduras, enquanto Aging teve um desempenho melhor com um número intermediário de molduras.

