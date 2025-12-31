import argparse
import pandas as pd
try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
except Exception:
    from fetch_data import fetch_stock_data

    class Table:
        def __init__(self, title=None):
            self.title = title
            self.columns = []
            self.rows = []

        def add_column(self, name, style=None, justify=None):
            self.columns.append(name)

        def add_row(self, *values):
            self.rows.append(values)

    class Console:
        def print(self, obj="", *args, **kwargs):
            if isinstance(obj, Table):
                if obj.title:
                    print(obj.title)
                if obj.columns:
                    print(" | ".join(obj.columns))
                    print("-" * max(1, len(" | ".join(obj.columns))))
                for row in obj.rows:
                    print(" | ".join(str(x) for x in row))
            else:
                print(obj, *args)

    console = Console()
else:

    from fetch_data import fetch_stock_data

from visualize import plot_price_trends, plot_correlation_heatmap, plot_returns_distribution


def risk_label(vol):
    if vol < 0.015:
        return "Low Risk 🟢"
    elif vol < 0.03:
        return "Medium Risk 🟡"
    else:
        return "High Risk 🔴"


def display_volatility(volatility_dict):
    table = Table(title="📊 Stock Volatility Summary")

    table.add_column("Stock", style="cyan", justify="center")
    table.add_column("Volatility", style="magenta", justify="center")
    table.add_column("Risk Profile", style="green", justify="center")

    for stock, vol in volatility_dict.items():
        table.add_row(
            stock,
            f"{vol:.4f}",
            risk_label(vol)
        )

    console.print(table)


def main(stocks):
    console.print("\n[bold blue]📈 Stock Volatility & Correlation Analyzer[/bold blue]\n")

    try:
        price_df = fetch_stock_data(stocks)
    except RuntimeError as e:
        console.print(f"[red]❌ Error:[/red] {e}")
        return

    if price_df.shape[0] < 2:
        console.print("[red]⚠️  Not enough data to compute returns.[/red]")
        return

    # Compute daily returns safely
    returns_df = price_df.pct_change().dropna()

    volatility = {}
    for stock in returns_df.columns:
        vol = returns_df[stock].std()
        volatility[stock] = vol

    display_volatility(volatility)
    corr_matrix = returns_df.corr()
    
    console.print("\n[bold cyan]📊 Correlation Matrix[/bold cyan]\n")
    console.print(corr_matrix.to_string())
    console.print("\n[bold yellow]📈 Generating visualizations...[/bold yellow]\n")
    
    try:
        console.print("[cyan]Plotting stock price trends...[/cyan]")
        plot_price_trends(price_df)
        
        console.print("[cyan]Plotting returns distribution...[/cyan]")
        plot_returns_distribution(returns_df)
        
        console.print("[cyan]Plotting correlation heatmap...[/cyan]")
        plot_correlation_heatmap(corr_matrix)
        
        console.print("\n[green]✓ Visualizations completed![/green]")
    except Exception as e:
        console.print(f"[red]Warning: Could not generate visualizations: {e}[/red]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stock Volatility & Correlation Analyzer")
    parser.add_argument("--stocks", nargs="+", required=True, help="List of stock tickers (e.g., AAPL MSFT TSLA)")
    
    args = parser.parse_args()
    main(args.stocks)

