# Simulação Predador-Presa: Lobos e Alces

Este repositório implementa uma simulação matemática da dinâmica populacional entre lobos e alces usando o método numérico de Runge-Kutta de 4ª ordem (RK4).

## Descrição

O programa simula a interação ecológica entre duas espécies usando o modelo predador-presa de Lotka-Volterra:

- **Alces (E)**: População de presas (em milhares)
- **Lobos (W)**: População de predadores (em milhares)

### Equações Diferenciais

O sistema é governado pelas seguintes equações:

```
dE/dt = r*E - a*E*W
dW/dt = -b*W + c*E*W
```

Onde:
- `r = 0.0325`: Taxa de crescimento natural dos alces
- `a = 0.8`: Taxa de predação (impacto dos lobos sobre os alces)
- `b = 0.6`: Taxa de mortalidade natural dos lobos
- `c = 0.05`: Taxa de crescimento dos lobos baseada no alimento disponível

### Condições Iniciais

- **Alces**: 18.000 indivíduos (18.0 mil)
- **Lobos**: 21 indivíduos (0.021 mil)
- **Período simulado**: 200 anos (começando em 1995)
- **Passo temporal**: 0.1 anos

## Uso

```bash
make run
```

## Dependências

As dependências estão listadas em `requirements.txt`:
- `numpy`: Computação numérica
- `pandas`: Manipulação de dados
- `matplotlib`: Geração de gráficos

## Resultados

A simulação gera os seguintes arquivos na pasta `out/`:

### Dados (`out/data/`)
- `populacoes_lobos_alces.csv`: Dados temporais das populações

### Gráficos (`out/graphs/`)
- `populacao_tempo_200anos.png`: Evolução das populações ao longo de 200 anos
- `populacao_tempo_15anos.png`: Detalhamento dos primeiros 15 anos
- `grafico_de_fase.png`: Diagrama de fase (Alces vs. Lobos)

## Estrutura do Projeto

```
.
├── main.py              # Script principal da simulação
├── requirements.txt     # Dependências Python
├── Makefile            # Comandos de execução
├── runge_kutta.pdf     # Documentação teórica
├── README.md           # Este arquivo
└── out/                # Resultados da simulação
    ├── data/           # Dados em CSV
    └── graphs/         # Gráficos em PNG
```

