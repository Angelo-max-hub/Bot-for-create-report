"""
Este é o script principal da automação.

O bot executa as seguintes etapas:
1. Conecta-se ao BotCity Maestro para obter parâmetros e gerenciar a tarefa.
2. Lê os dados de frequência de um arquivo CSV usando pandas.
3. Valida os dados para garantir que não há valores nulos.
4. Gera um relatório em PDF com os dados de frequência.
5. Envia o relatório gerado por e-mail para um destinatário especificado.
6. Notifica o Maestro sobre o sucesso ou falha da execução.

Para mais informações sobre como configurar e executar o bot, consulte o README.md.
"""

from botcity.maestro import BotMaestroSDK, AutomationTaskFinishStatus, AlertType
import pandas as pd
from src.errors.errors import ErrorProtocol
from src.relatorio.gerar_relatorio import report
from src.send_email.send_email import enviar_relatorio
from src.log.registrar_logs import LogFile
import settings as s

# Desabilita erros caso não esteja conectado ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = True

# Ponto de entrada principal da automação
def main():
    """Função principal que orquestra a execução do bot.

    Developer's Note:
        A lógica da automação é executada sequencialmente dentro do bloco `try`.
        Para adicionar um novo passo, insira sua lógica na ordem correta entre os
        passos existentes. Certifique-se de adicionar mensagens de log (`log_file.log_message`)
        para cada novo passo, para facilitar o rastreamento e a depuração.
        Se o novo passo for crítico e puder falhar, envolva-o em seu próprio
        bloco `try...except` e use o `error_protocol` para tratar a falha.
    """
    # Instancia o SDK do Maestro a partir dos argumentos do sistema
    maestro = BotMaestroSDK.from_sys_args()
    # Obtém os detalhes da execução atual
    execution = maestro.get_execution()

    # Inicializa o gerenciador de logs
    log_file = LogFile(execution)
    # Inicializa o protocolo de tratamento de erros
    error_protocol = ErrorProtocol(maestro, log_file)

    try:
        # --- 1. Leitura dos Dados ---
        log_file.log_message("Extraindo dados da tabela...")
        path_to_data_table = s.PATH_TO_DATA_TABLE.get_value_as_str(execution)
        frequencia_df = pd.read_csv(path_to_data_table)

        # --- 2. Validação dos Dados ---
        log_file.log_message('Procurando por valores nulos...')
        if frequencia_df.isna().any().any():
            # Se houver valores nulos, registra um erro e encerra
            error_protocol.send_and_register_error(
                "Há valores nulos nos dados. Corrija e tente novamente.",
                ValueError('Valores nulos encontrados nos dados')
            )

        # --- 3. Geração do Relatório ---
        log_file.log_message("Gerando o PDF do relatório...")
        relatorio = report(execution)
        relatorio.given_report(frequencia_df)

        # --- 4. Envio do E-mail ---
        log_file.log_message("Enviando o relatório por e-mail...")
        enviar_relatorio(execution)

        # --- 5. Notificação de Sucesso ---
        log_file.log_message("Tarefa concluída com sucesso.")
        maestro.alert(
            task_id=execution.task_id,
            title="Relatório Enviado",
            message="Um relatório da frequência da turma A foi enviado ao professor Ângelo por e-mail.",
            alert_type=AlertType.INFO
        )
        # Finaliza a tarefa no Maestro como sucesso
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Tarefa concluída com sucesso."
        )

    except Exception as e:
        # Em caso de qualquer exceção não tratada, aciona o protocolo de erro
        error_protocol.send_and_register_error(f"Ocorreu um erro inesperado: {e}", e)

if __name__ == '__main__':
    main()