from rich.console import Console

console = Console()

def info(msg):
    console.print(f"[green]{msg}[/green]")

def warn(msg):
    console.print(f"[yellow]{msg}[/yellow]")

def error(msg):
    console.print(f"[red]{msg}[/red]")