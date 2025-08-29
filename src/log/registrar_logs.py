"""
Este módulo fornece a classe LogFile para gerenciar a criação e escrita de logs
durante a execução do bot.
"""

from datetime import datetime
import os
from botcity.maestro import BotExecution
import settings as s

class LogFile:
    """Gerencia a criação e o registro de mensagens em um arquivo de log.

    A classe verifica se um arquivo de log já existe. Se não, um novo arquivo é criado.
    As mensagens de log são sempre prefixadas com a data e hora atuais.

    Attributes:
        path_file (str): O caminho para o arquivo de log, obtido dos parâmetros da automação.
        horario_aut (str): A data e hora formatadas para serem usadas no log.

    Developer's Note:
        Se for necessário um formato de log diferente ou uma lógica de rotação de arquivos,
        você pode adicionar novos métodos a esta classe ou modificar o método `log_message`.
        Por exemplo, para adicionar um nível de log (INFO, WARNING), você poderia
        modificar `log_message` para aceitar um parâmetro `level` e formatar a string
        de acordo.
    """
    def __init__(self, execution: BotExecution) -> None:
        """Inicializa a classe LogFile.

        Args:
            execution (BotExecution): O objeto de execução da tarefa do Maestro.
        """
        self.path_file = s.PATH_TO_LOGFILE.get_value_as_str(execution)
        agora = str(datetime.now()) + "\n"
        self.horario_aut = f"Horário: {agora}"
        
        # Se não existir um arquivo para logs, criar um com conteúdo vazio.
        if not os.path.exists(self.path_file):
            self._write_log_file("")

    def log_message(self, contents: str):
        """Registra uma nova mensagem no arquivo de log.

        A mensagem é adicionada ao final do arquivo, prefixada com o horário.

        Args:
            contents (str): O conteúdo da mensagem de log a ser registrada.
        """
        with open(self.path_file, "a") as f:
            f.write(self.horario_aut + contents + "...\n")
    
    def _write_log_file(self, contents: str):
        """Escreve (ou sobrescreve) o conteúdo do arquivo de log.

        Este método é usado internamente para criar o arquivo de log se ele não existir.

        Args:
            contents (str): O conteúdo a ser escrito no arquivo.
        """
        with open(self.path_file, "w") as f:
            f.write(contents)