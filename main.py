import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

matplotlib.use('Agg')

# --------------------------
# Parâmetros do sistema
# --------------------------
r = 0.0325  # Crescimento dos alces (taxa positiva)
a = 0.8     # Impacto dos lobos sobre os alces (taxa negativa)
b = 0.6     # Mortalidade natural dos lobos
c = 0.05    # Crescimento dos lobos com base em alimento (alces)

# Condições iniciais (populações em milhares)
E0 = 18.0   # Alces
W0 = 0.021  # Lobos (21 indivíduos)

# Configuração da simulação
h = 0.1     # Passo (anos)
T = 200     # Tempo total (anos)


def dE_dt(E: float, W: float) -> float:
    """Derivada de E em relação ao tempo."""
    return r * E - a * E * W


def dW_dt(E: float, W: float) -> float:
    """Derivada de W em relação ao tempo."""
    return -b * W + c * E * W


# --------------------------
# Método de Runge-Kutta (RK4)
# --------------------------

def runge_kutta(E0: float, W0: float, h: float, T: float):
    t_values = [0.0]
    E_values = [E0]
    W_values = [W0]

    t = 0.0
    E = E0
    W = W0

    while t < T:
        k1_E = dE_dt(E, W)
        k1_W = dW_dt(E, W)

        k2_E = dE_dt(E + 0.5 * h * k1_E, W + 0.5 * h * k1_W)
        k2_W = dW_dt(E + 0.5 * h * k1_E, W + 0.5 * h * k1_W)

        k3_E = dE_dt(E + 0.5 * h * k2_E, W + 0.5 * h * k2_W)
        k3_W = dW_dt(E + 0.5 * h * k2_E, W + 0.5 * h * k2_W)

        k4_E = dE_dt(E + h * k3_E, W + h * k3_W)
        k4_W = dW_dt(E + h * k3_E, W + h * k3_W)

        E += (h / 6.0) * (k1_E + 2 * k2_E + 2 * k3_E + k4_E)
        W += (h / 6.0) * (k1_W + 2 * k2_W + 2 * k3_W + k4_W)
        t += h

        t_values.append(t)
        E_values.append(E)
        W_values.append(W)

    return np.array(t_values), np.array(E_values), np.array(W_values)


# --------------------------
# Execução da simulação
# --------------------------

def main() -> None:
    t_vals, E_vals, W_vals = runge_kutta(E0, W0, h, T)

    # Estrutura de saídas
    base_dir = Path("out")
    data_dir = base_dir / "data"
    graphs_dir = base_dir / "graphs"

    data_dir.mkdir(parents=True, exist_ok=True)
    graphs_dir.mkdir(parents=True, exist_ok=True)

    # --------------------------
    # Salvar dados em CSV
    # --------------------------
    df = pd.DataFrame({
        "Ano": t_vals + 1995,
        "Alces (mil)": E_vals,
        "Lobos (mil)": W_vals,
    })
    csv_path = data_dir / "populacoes_lobos_alces.csv"
    df.to_csv(csv_path, index=False)

    # --------------------------
    # Gráficos
    # --------------------------
    plt.figure()
    plt.plot(df["Ano"], df["Alces (mil)"], label="Alces")
    plt.plot(df["Ano"], df["Lobos (mil)"], label="Lobos")
    plt.xlabel("Ano")
    plt.ylabel("Populacao (milhares)")
    plt.title("Populacao de Alces e Lobos - 200 anos")
    plt.legend()
    plt.grid(True)
    plt.savefig(graphs_dir / "populacao_tempo_200anos.png")
    plt.close()

    # Graficos primeiros 15 anos
    plt.figure()
    n15 = int(15 / h)
    plt.plot(df["Ano"].iloc[:n15], df["Alces (mil)"].iloc[:n15], label="Alces")
    plt.plot(df["Ano"].iloc[:n15], df["Lobos (mil)"].iloc[:n15], label="Lobos")
    plt.xlabel("Ano")
    plt.ylabel("Populacao (milhares)")
    plt.title("Populacao nos primeiros 15 anos")
    plt.legend()
    plt.grid(True)
    plt.savefig(graphs_dir / "populacao_tempo_15anos.png")
    plt.close()

    # Grafico de fase
    plt.figure()
    plt.plot(E_vals, W_vals)
    plt.xlabel("Alces (milhares)")
    plt.ylabel("Lobos (milhares)")
    plt.title("Grafico de Fase: Alces vs. Lobos")
    plt.grid(True)
    plt.savefig(graphs_dir / "grafico_de_fase.png")
    plt.close()

    print("Simulacao concluida. Dados e imagens salvos com sucesso.")


if __name__ == "__main__":
    main()
