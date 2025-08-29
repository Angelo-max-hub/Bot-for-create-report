"""
Módulo para orquestrar o envio do e-mail com o relatório em anexo.
"""

from botcity.maestro import BotExecution
from botcity.plugins.gmail import BotGmailPlugin
from os.path import abspath
import settings as s

def enviar_relatorio(execution: BotExecution):
    """Envia o relatório em PDF por e-mail.

    Esta função obtém os parâmetros de automação, adquire uma instância autenticada
    do plugin do Gmail e envia o e-mail com o relatório em anexo.

    Developer's Note:
        Para modificar o conteúdo do e-mail, altere as variáveis `subject` e `body_email`
        nesta função. Para adicionar mais anexos, adicione o caminho absoluto do arquivo
        à lista `anexo`. A lógica de autenticação (`BotGmailPlugin`)
        também está aqui; certifique-se de que os parâmetros `PATH_TO_CREDENTIALS` e
        `EMAIL_PESSOAL` estejam corretamente configurados no Maestro.

    Args:
        execution (BotExecution): O objeto de execução da tarefa do Maestro.
    """
    
    # Obtém os parâmetros da automação
    EMAIL_PESSOAL = s.EMAIL_PESSOAL.get_value_as_str(execution)
    EMAIL_DESTINATARIO = s.EMAIL_DESTINATARIO.get_value_as_str(execution)
    ASSUNTO_EMAIL = s.ASSUNTO_EMAIL.get_value_as_str(execution)
    PATH_TO_OUTPUT = s.PATH_TO_OUTPUT.get_value_as_str(execution)
    PATH_TO_CREDENTIALS = s.PATH_TO_CREDENTIALS.get_value_as_str(execution)

    # Instância do Gmail.
    gmail = BotGmailPlugin(PATH_TO_CREDENTIALS, EMAIL_PESSOAL)

    # Define os atributos da mensagem
    to = [EMAIL_DESTINATARIO]
    subject = ASSUNTO_EMAIL
    body_email = ("""Bom dia, professor Ângelo.

        Segue em anexo o relatório.

        Atenciosamente, Robô.""")
    anexo = [abspath(PATH_TO_OUTPUT)]

    # Envia a mensagem de e-mail
    gmail.send_message(
        subject=subject,
        text_content=body_email,
        to_addrs=to,
        attachments=anexo
    )

    print("E-mail foi enviado com sucesso.")
