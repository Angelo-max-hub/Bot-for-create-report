"""
Este módulo é responsável pela geração do relatório de frequência em formato PDF.

Utiliza a biblioteca reportlab para criar um documento com capa, página de descrição
e uma tabela com os dados de frequência dos alunos.
"""

from reportlab.platypus import Spacer, Paragraph, SimpleDocTemplate, PageBreak, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import pandas as pd
from src.relatorio.utils.mystyles import get_styles
from src.relatorio.utils.getdata import data_atual
import settings as s
from botcity.maestro import BotExecution

class report:
    """Gera um relatório em PDF a partir de um DataFrame do pandas.

    A classe constrói um documento PDF com múltiplos elementos, incluindo parágrafos,
    espaçadores e tabelas, organizados em uma "história" (story) que é então
    renderizada pela biblioteca reportlab.

    Attributes:
        doc (SimpleDocTemplate): O template do documento PDF.
        styles (StyleSheet1): A folha de estilos para formatação do texto.
        story (list): A lista de elementos que comporão o PDF.
    """
    def __init__(self, execution: BotExecution):
        """Inicializa a classe report.

        Args:
            execution (BotExecution): O objeto de execução da tarefa do Maestro.
        """
        PATH_TO_OUTPUT = s.PATH_TO_OUTPUT.get_value(execution)
        self.doc = SimpleDocTemplate(PATH_TO_OUTPUT)
        self.styles = get_styles()
        self.story = []
        
    def given_report(self, df: pd.DataFrame):
        """Constrói e gera o relatório PDF com base nos dados fornecidos.

        Developer's Note:
            A ordem das seções no PDF é definida pela ordem em que são adicionadas
            à `self.story` aqui. Para adicionar uma nova página ou seção:
            1. Crie um novo método nesta classe (ex: `minha_nova_pagina()`) que retorne
               uma lista de elementos `reportlab` (como `Paragraph`, `Spacer`, `Table`).
            2. Chame este novo método dentro de `given_report` e adicione o resultado
               à "história" usando `self._add_struct(self.minha_nova_pagina())`.

        Args:
            df (pd.DataFrame): O DataFrame contendo os dados de frequência.
        """
        # Converte o DataFrame para o formato de lista necessário para a tabela
        for_table = self._df_to_list(df)
    
        # Adiciona a capa ao relatório
        self._add_struct(self.Capa())

        # Adiciona a página de descrição da automação
        self._add_struct(self.pagina_descricao_automocao())

        # Adiciona a página com a tabela de frequência
        self._add_struct(self.tabela_da_classe(for_table))
    
        # Imprime uma mensagem de status no console
        self._print_info()

        # Constrói o PDF a partir da "história" de elementos
        self.doc.build(self.story)

    # Métodos para criar as seções do relatório
    def Capa(self) -> list:
        """Cria os elementos da página de capa do relatório.

        Returns:
            list: Uma lista de elementos reportlab para a capa.
        """
        posicao_central_vertical = (A4[0] / 2) - 7
        body = [
            Paragraph("ESCOLA RAIMUNDA CONCEIÇÃO", self.styles['titulo-central-negrito']),
            Spacer(0, posicao_central_vertical),
            Paragraph("FREQUENCIA DA TURMA A", self.styles['titulo-central']),
            Spacer(0, posicao_central_vertical - 5),
            Paragraph(data_atual(), self.styles['titulo-central']),
            PageBreak()
        ]
        return body

    def tabela_da_classe(self, data: list) -> list:
        """Cria os elementos da página que contém a tabela de frequência.

        Args:
            data (list): Os dados a serem exibidos na tabela, formatados como lista de listas.

        Returns:
            list: Uma lista de elementos reportlab para a página da tabela.
        """
        body = [
            Paragraph("Frequencia dos alunos", self.styles['corpo-do-texto']),
            Spacer(0, 2 * cm),
            Table(data),
            PageBreak()
        ]
        return body

    def pagina_descricao_automocao(self) -> list:
        """Cria a página de descrição com informações sobre a automação.

        Returns:
            list: Uma lista de elementos reportlab para a página de descrição.
        """
        text_context = ("""Este relatório é resultado de um projeto de automação RPA que produz um arquivo
        relacionado a frequência de uma turma (fictícia) e o manda via e-mail a um professor
        (fictício também.). O fiz para me aprimorar nesta área e demonstrar minhas habilidades. Essa
        descrição serve pra confirmar que o relatório que o bot produz de fato tem uma formatação
        possivelmente confusa e sem sentido. Isso é porque não sei exatamente como deveria ser um relatório
        neste contexto, e decidi não separar tanto tempo assim para formatação ou estrutura.""")
        body = [
            Paragraph("Observações sobre a automação e o relatório".upper(), self.styles['titulo-central']),
            Paragraph(text_context, self.styles['corpo-do-texto']),
            PageBreak()
        ]
        return body

    # Funções utilitárias internas
    def _df_to_list(self, df: pd.DataFrame) -> list:
        """Converte um DataFrame do pandas em uma lista de listas.

        Args:
            df (pd.DataFrame): O DataFrame a ser convertido.

        Returns:
            list: Uma lista contendo os cabeçalhos e os dados do DataFrame.
        """
        return [df.columns.tolist()] + df.values.tolist()
    
    def _add_struct(self, struct: list):
        """Adiciona uma lista de elementos à "história" do PDF.

        Args:
            struct (list): A lista de elementos reportlab a ser adicionada.
        """
        self.story.extend(struct)
        
    def _print_info(self):
        """Imprime uma mensagem de sucesso no console."""
        print('PDF gerado com sucesso.')