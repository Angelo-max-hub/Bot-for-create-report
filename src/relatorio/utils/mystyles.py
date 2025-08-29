"""
Módulo para definir e customizar os estilos de parágrafo usados no relatório PDF.

Este módulo utiliza a biblioteca reportlab para criar e configurar estilos como
título, corpo de texto, etc., garantindo uma formatação consistente no documento.
"""

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, StyleSheet1
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def get_styles() -> StyleSheet1:
    """Cria e retorna uma folha de estilos customizada para o relatório.

    Developer's Note:
        Para adicionar um novo estilo de parágrafo, siga estes passos:
        1. Crie uma nova função que aceite `styles: StyleSheet1` como argumento e
           retorne um `ParagraphStyle`. Inspire-se nas funções existentes
           (`titulo_central`, `corpo_do_texto`, etc.).
        2. Na nova função, configure as propriedades do estilo (ex: `name`, `fontName`,
           `fontSize`, `alignment`).
        3. Dentro da função `get_styles`, chame sua nova função para criar o estilo
           e adicione-o à folha de estilos com `my_styles.add(...)`.
        4. Agora você pode usar o novo estilo no `gerar_relatorio.py` referenciando-o
           pelo nome (ex: `self.styles['meu-novo-estilo']`).

    Returns:
        StyleSheet1: Um objeto contendo todos os estilos de parágrafo configurados.
    """
    my_styles = getSampleStyleSheet()
    _setup_styles_global(my_styles)
    
    # Adiciona estilos customizados à folha
    my_styles.add(titulo_central_negrito(my_styles))
    my_styles.add(titulo_central(my_styles))
    my_styles.add(corpo_do_texto(my_styles))
    
    return my_styles

def _setup_styles_global(styles: StyleSheet1):
    """Configura as propriedades globais dos estilos.

    Args:
        styles (StyleSheet1): A folha de estilos a ser modificada.
    """
    # Configurações para o estilo 'Normal'
    styles['Normal'].fontName = "Times-Roman"
    styles['Normal'].fontSize = 12
    styles['Normal'].leading = styles['Normal'].fontSize * 1.5
    
def titulo_central_negrito(styles: StyleSheet1) -> ParagraphStyle:
    """Cria um estilo de parágrafo para título centralizado e em negrito.

    Args:
        styles (StyleSheet1): A folha de estilos pai.

    Returns:
        ParagraphStyle: O estilo de parágrafo configurado.
    """
    return ParagraphStyle(
        name='titulo-central-negrito',
        fontName="Times-Roman",
        alignment=TA_CENTER,
        fontSize=12,
        parent=styles['Normal']
    )

def titulo_central(styles: StyleSheet1) -> ParagraphStyle:
    """Cria um estilo de parágrafo para título centralizado.

    Args:
        styles (StyleSheet1): A folha de estilos pai.

    Returns:
        ParagraphStyle: O estilo de parágrafo configurado.
    """
    return ParagraphStyle(
        name="titulo-central",
        parent=styles['Normal'],
        alignment=TA_CENTER
    )

def corpo_do_texto(styles: StyleSheet1) -> ParagraphStyle:
    """Cria um estilo de parágrafo para o corpo de texto com alinhamento à esquerda.

    Args:
        styles (StyleSheet1): A folha de estilos pai.

    Returns:
        ParagraphStyle: O estilo de parágrafo configurado.
    """
    return ParagraphStyle(
        name="corpo-do-texto",
        parent=styles['Normal'],
        alignment=TA_LEFT
    )