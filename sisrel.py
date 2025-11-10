import random
from datetime import datetime, timedelta
from typing import List

from rich.console import Console
from rich.panel import Panel

console = Console()


class Venda:
    """Representa uma venda simples com produto, valor e data."""
    def __init__(self, produto: str, valor: float, data: datetime):
        self.produto = produto
        self.valor = valor
        self.data = data

    def __str__(self) -> str:
        return f"{self.produto} - R${self.valor:.2f} em {self.data.strftime('%d/%m/%Y')}"


def header() -> None:
    """Mostra um cabeçalho bonito usando Rich."""
    titulo = "[bold cyan]Seja bem-vindo ao SISREL[/bold cyan]"
    console.print(Panel(titulo, expand=False))


def gerar_vendas(qtd: int) -> List[Venda]:
    """Gera uma lista de vendas aleatórias nos últimos 30 dias."""
    produtos = ['Camiseta', 'Calça', 'Tênis', 'Boné']
    vendas: List[Venda] = []
    now = datetime.now()
    for _ in range(qtd):
        produto = random.choice(produtos)
        valor = random.uniform(50, 500)
        dias_atras = random.randint(1, 30)
        data = now - timedelta(days=dias_atras)
        vendas.append(Venda(produto, valor, data))
    return vendas


def calcular_media(vendas: List[Venda]) -> float:
    """Calcula a média de valores das vendas."""
    if not vendas:
        raise ValueError("Lista de vendas vazia: não é possível calcular a média.")
    total = sum(v.valor for v in vendas)
    return total / len(vendas)


def filtrar_por_produto(vendas: List[Venda], nome_produto: str) -> List[Venda]:
    """Filtra vendas pelo nome do produto (igualdade exata)."""
    return [v for v in vendas if v.produto == nome_produto]


def relatorio(vendas: List[Venda]) -> None:
    """Imprime um relatório simples das vendas e da média."""
    console.print("\n[bold]Relatório de Vendas diárias:[/bold]\n")
    for v in vendas:
        console.print(v)
    media = round(calcular_media(vendas), 2)
    console.print(f"\nMédia das vendas: [green]R$ {media}[/green]")


def main() -> None:
    header()
    vendas = gerar_vendas(10)
    vendas_tenis = filtrar_por_produto(vendas, 'Tênis')
    console.print("\n[bold]Vendas de Tênis:[/bold]")
    for v in vendas_tenis:
        console.print(v)
    console.print("\n[bold]Análise geral:[/bold]")
    # aqui eh um bug escondido (mantido como easter egg para aula)
    relatorio(vendas)
    console.print("\n" + "-" * 50)
    console.print("Programa finalizado")
    console.print("-" * 50)
    console.print("Tenha um bom dia!\n")


if __name__ == '__main__':
    main()
