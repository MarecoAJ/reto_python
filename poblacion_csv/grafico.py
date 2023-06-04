import matplotlib.pyplot as plt

def grafico_barra(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def grafico_torta(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()
if __name__ == "__main__":
    grafico_barra()
    grafico_torta()
