# Bot Gerador de Relatório de Frequência

## Introdução

Este é um bot que, vinculado ao BotCity Orquestrator, cria um relatório de frequência de uma turma fictícia e o envia por e-mail a um professor fictício. Para usar este bot, é essencial ter uma conta no Botcity, com o Orquestrador completamente configurado. Veja mais sobre isso na [documentação do BotCity](https://documentation.botcity.dev/).

Este projeto foi desenvolvido para demonstrar meu conhecimento da ferramenta BotCity. Portanto, talvez ele não possa ser usado como uma ferramenta genérica sem modificações no código.

## Uso

Para ver o bot em ação, siga estas etapas:

1.  Faça um pull request do repositório.
2.  Crie um projeto no Google Cloud e habilite a API do Gmail.
3.  Autorize a conta que será usada para enviar o relatório.
4.  Coloque as credenciais geradas em `resources/credenciais_oauth.json`, ou coloque em outro caminho e altere o valor de `PATH_TO_CREDENTIALS`. Veja em **Parâmetros de Automação** abaixo.
5.  Adicione um arquivo CSV com os dados de frequência da turma. O caminho e o nome do arquivo devem corresponder ao valor do parâmetro `PATH_TO_DATA_TABLE` (o padrão é `resources/frequenciaTurmaA.csv`).

## Parâmetros de Automação

Os parâmetros de automação podem ser configurados no BotCity Orquestrator para alterar o comportamento do bot sem a necessidade de modificar o código.

### Parâmetros Obrigatórios

Estes parâmetros precisam ser configurados no Orquestrador para que o bot funcione corretamente.

*   `EMAIL_PESSOAL`: O endereço de e-mail que será usado para enviar o relatório.
*   `EMAIL_DESTINATARIO`: O endereço de e-mail do destinatário do relatório.
*   `ASSUNTO_EMAIL`: O assunto do e-mail.

### Parâmetros Opcionais

Estes parâmetros têm valores padrão, mas podem ser substituídos no Orquestrador.

*   `PATH_TO_CREDENTIALS`: O caminho para o arquivo de credenciais do OAuth do Google.
    *   **Padrão**: `resources/credenciais_oauth.json`
*   `PATH_TO_LOGFILE`: O caminho para o arquivo de log.
    *   **Padrão**: `resources/logs.txt`
*   `PATH_TO_OUTPUT`: O caminho onde o relatório em PDF será salvo.
    *   **Padrão**: `resources/report.pdf`
*   `PATH_TO_DATA_TABLE`: O caminho para o arquivo de dados (CSV) com as informações de frequência.
    *   **Padrão**: `resources/frequenciaTurmaA.csv`
