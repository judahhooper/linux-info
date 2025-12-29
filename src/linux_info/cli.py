import typer
from .linux_info import linux_info

app = typer.Typer()
app.command()(linux_info)

def main():
    app()

if __name__ == "__main__":
    main()

