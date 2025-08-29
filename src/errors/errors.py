"""
Este módulo define o protocolo de tratamento de erros da automação.
"""

from botcity.maestro import AlertType, BotMaestroSDK, BotExecution
from src.log.registrar_logs import LogFile

class ErrorProtocol:
    """Centraliza a lógica de tratamento de erros da automação.

    Quando um erro ocorre, esta classe é responsável por:
    1. Enviar o erro para o BotCity Maestro.
    2. Enviar um alerta para o Maestro.
    3. Registrar a exceção no arquivo de log.
    4. Encerrar a execução do bot para prevenir comportamento inesperado.

    Developer's Note:
        Para usar este protocolo em uma nova parte do código que pode gerar uma exceção,
        envolva o código em um bloco `try...except` e chame o método
        `error_protocol.send_and_register_error()` no bloco `except`.

        Exemplo:
        ```python
        try:
            # Seu código propenso a erros aqui
            ...
        except Exception as e:
            error_protocol.send_and_register_error("Descrição do erro para o Maestro", e)
        ```
    """
    def __init__(self, maestro: BotMaestroSDK, log_file: LogFile):
        """Inicializa a classe ErrorProtocol.

        Args:
            maestro (BotMaestroSDK): A instância do SDK do BotCity Maestro.
            log_file (LogFile): A instância do gerenciador de logs.
        """
        self._maestro = maestro
        self._execution: BotExecution = self._maestro.get_execution()
        self.log_file = log_file
        
    def send_and_register_error(self, message: str, e: Exception):
        """Envia, alerta, registra o erro e encerra a execução.

        Args:
            message (str): A mensagem descritiva do erro para o alerta do Maestro.
            e (Exception): O objeto da exceção que foi capturada.
        """
        # Envia o erro para o orquestrador com o log como anexo.
        self._maestro.error(
            task_id=self._execution.task_id,
            exception=e,
            attachments=[self.log_file.path_file]
        )
        # Envia um alerta para o orquestrador.
        self._maestro.alert(
            task_id=self._execution.task_id,
            title="Erro de execução",
            message=message,
            alert_type=AlertType.ERROR
        )

        # Registra o erro no arquivo de log.
        self.log_file.log_message(f"ERRO DE EXECUÇÃO...\n{e}")

        # Encerra o programa.
        exit(1)