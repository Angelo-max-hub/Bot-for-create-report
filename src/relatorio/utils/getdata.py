"""
Módulo utilitário para obter a data e hora atuais em um formato específico.

Developer's Note:
    Se precisar de outros formatos de data ou informações relacionadas ao tempo,
    você pode adicionar novas funções a este módulo. Por exemplo, uma função
    `get_hora_atual()` que retorna a hora formatada.
"""

from datetime import datetime as dt

def data_atual() -> str:
    """Retorna a data atual formatada como 'dd/mm/YYYY'.

    Returns:
        str: A data atual no formato de string.
    """
    data = dt.now().strftime("%d/%m/%Y")
    return data

if __name__ == "__main__":
    print(data_atual())