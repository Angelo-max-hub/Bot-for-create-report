"""
Este módulo centraliza a definição e o gerenciamento dos parâmetros da automação,
facilitando o acesso e a manutenção.

A classe `ParameterOfAutomation` permite definir parâmetros com um nome e um valor padrão,
que podem ser sobrescritos no BotCity Maestro.

Para usar um parâmetro em outros módulos:
1. Importe o módulo: `import settings as s`
2. Acesse o parâmetro e obtenha seu valor: `meu_parametro = s.NOME_DO_PARAMETRO.get_value(execution)`

Developer's Note:
    Para adicionar um novo parâmetro de automação, crie uma nova instância da classe
    `ParameterOfAutomation` neste arquivo, seguindo os exemplos abaixo.
    - Para parâmetros obrigatórios, defina `default_value=None`.
    - Para parâmetros opcionais, forneça um valor padrão para `default_value`.
"""
from dataclasses import dataclass
from botcity.maestro import BotExecution

@dataclass(frozen=True)
class ParameterOfAutomation:
    """Representa um parâmetro de automação com um nome e valor padrão.

    Attributes:
        name (str): O nome do parâmetro, usado para identificá-lo no Maestro.
        default_value (object): O valor padrão a ser usado se o parâmetro não for
                                fornecido pelo Maestro.
    """
    name: str
    default_value: object

    def get_value(self, execution: BotExecution) -> object:
        """Retorna o valor do parâmetro do Maestro ou o valor padrão.

        Args:
            execution (BotExecution): O objeto de execução da tarefa do Maestro.

        Returns:
            object: O valor do parâmetro.
        """
        return execution.parameters.get(self.name, self.default_value)

    def get_value_as_str(self, execution: BotExecution) -> str:
        """Retorna o valor do parâmetro do Maestro como uma string.

        Args:
            execution (BotExecution): O objeto de execução da tarefa do Maestro.

        Returns:
            str: O valor do parâmetro convertido para string.
        """
        return str(
            execution.parameters.get(self.name, self.default_value)
        )

# ====================================================
# PARÂMETROS OBRIGATÓRIOS
# (Devem ser configurados no Maestro)
# ====================================================
EMAIL_PESSOAL = ParameterOfAutomation(name="EMAIL_PESSOAL", default_value=None)
EMAIL_DESTINATARIO = ParameterOfAutomation(name="EMAIL_DESTINATARIO", default_value=None)
ASSUNTO_EMAIL = ParameterOfAutomation(name="ASSUNTO_EMAIL", default_value=None)

# ====================================================
# PARÂMETROS OPCIONAIS
# (Possuem um valor padrão, mas podem ser sobrescritos no Maestro)
# ====================================================
PATH_TO_CREDENTIALS: ParameterOfAutomation = ParameterOfAutomation(
    name="PATH_TO_CREDENTIALS",
    default_value="resources/credenciais_oauth.json"
)

PATH_TO_LOGFILE: ParameterOfAutomation = ParameterOfAutomation(
    name="PATH_TO_LOGFILE",
    default_value="resources/logs.txt"
)

PATH_TO_OUTPUT: ParameterOfAutomation = ParameterOfAutomation(
    name="PATH_TO_OUTPUT",
    default_value="resources/report.pdf"
)

PATH_TO_DATA_TABLE: ParameterOfAutomation = ParameterOfAutomation(
    name="PATH_TO_DATA_TABLE",
    default_value="resources/frequenciaTurmaA.csv"
)