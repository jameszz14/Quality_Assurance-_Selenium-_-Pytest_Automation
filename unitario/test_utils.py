from utils import validar_email
from rich import print
from rich.panel import Panel

def checar_email(email, esperado):
    resultado = validar_email(email)
    if resultado == esperado:
        print(Panel.fit(f"[green]✔ PASSOU[/green] '{email}' → {resultado}"))
    else:
        print(Panel.fit(f"[red]✘ FALHOU[/red] '{email}' → esperado {esperado}, obtido {resultado}"))
        assert resultado == esperado, f"Falhou para '{email}': esperado {esperado}, obtido {resultado}"

def test_emails():
    # Testes válidos
    checar_email("teste@exemplo.com", True)
    checar_email("teste@exemplo.com.br", True)
    checar_email("teste@exemplo123.com", True)

    # Testes inválidos
    checar_email("", False)
    checar_email("teste.exemplo.com", False)
    checar_email("teste@exemplo", False)
    checar_email("@exemplo.com", False)
    checar_email("teste@.com", False)
    checar_email("teste @exemplo.com", False)
    checar_email("teste@exemplo .com", False)

if __name__ == "__main__":
    test_emails()
    print("\n[bold green]Todos os testes executados.[/bold green]")
# This code is a test suite for the email validation function.
# It checks various email formats against expected results and prints the outcome.
# If the validation fails, it raises an assertion error with a detailed message.
# It uses the `rich` library to format the output in a visually appealing way.