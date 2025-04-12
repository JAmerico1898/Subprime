import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
import base64
from io import BytesIO
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet, Range1d
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral8
import streamlit.components.v1 as components
from bokeh.embed import file_html
from bokeh.resources import CDN


# Configuração da página
st.set_page_config(
    page_title="Crise Subprime: Cronologia e Impactos",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Função para aplicar estilo CSS personalizado
def local_css():
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 1rem;
            background-color: #F0F7FF;
            padding: 1rem;
            border-radius: 10px;
        }
        .sub-header {
            font-size: 1.8rem;
            font-weight: 600;
            color: #2563EB;
            margin-top: 1rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #BFDBFE;
            padding-bottom: 0.5rem;
        }
        .chart-title {
            font-size: 1.3rem;
            font-weight: 500;
            color: #1E40AF;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .info-box {
            background-color: #EFF6FF;
            padding: 1rem;
            border-radius: 5px;
            border-left: 5px solid #3B82F6;
            margin-bottom: 1rem;
        }
        .timeline-item {
            margin-bottom: 0.8rem;
            padding: 0.8rem;
            border-radius: 5px;
            border-left: 3px solid #3B82F6;
            background-color: #F3F4F6;
        }
        .timeline-date {
            font-weight: 600;
            color: #1E40AF;
        }
        .timeline-description {
            margin-top: 0.3rem;
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            font-size: 0.8rem;
            color: #6B7280;
            border-top: 1px solid #E5E7EB;
        }
        .tab-content {
            padding: 1rem;
            background-color: #F9FAFB;
            border-radius: 5px;
            margin-top: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Título principal
st.markdown('<div class="main-header">Crise Subprime: Cronologia e Impactos Globais</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
Este aplicativo interativo apresenta uma análise detalhada da Crise Subprime de 2008, 
incluindo sua cronologia, causas, impactos globais e lições aprendidas. 
Navegue pelas diferentes seções usando o menu lateral.
</div>
""", unsafe_allow_html=True)

# Barra lateral com navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Selecione uma seção:",
    ["Introdução", 
     "Linha do Tempo", 
     "Bolha Imobiliária", 
     "Impacto Global",
     "Securitização",
     "Respostas Regulatórias",
     "Lições Aprendidas"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Sobre o aplicativo**

Este aplicativo foi desenvolvido como material didático para aulas sobre crises financeiras.

© 2025 - Prof. José Américo – Coppead
""")

# Conteúdo da página de Introdução
if page == "Introdução":
    st.markdown('<div class="sub-header">Visão Geral da Crise Subprime</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        A crise subprime de 2008 foi a mais severa crise financeira desde a Grande Depressão, 
        causando profundos impactos na economia global e mudando fundamentalmente o sistema 
        financeiro internacional.
        
        ### O que foi a crise subprime?
        
        A crise originou-se no mercado imobiliário dos Estados Unidos, centrada nos empréstimos 
        hipotecários de alto risco (subprime) concedidos a tomadores com histórico de crédito 
        questionável. A securitização desses empréstimos em instrumentos financeiros complexos 
        espalhou o risco pelo sistema financeiro global.
        
        ### Por que estudar esta crise?
        
        * Revela vulnerabilidades do sistema financeiro moderno
        * Demonstra como problemas em um setor podem se propagar globalmente
        * Levou a mudanças fundamentais na regulação financeira
        * Oferece lições valiosas para prevenir futuras crises
        
        Explore as diferentes seções deste aplicativo para entender a cronologia, as causas, 
        os impactos e as consequências desta crise histórica.
        """)
    
    with col2:
        st.markdown("""
        ### Fatos-chave
        
        * **Prejuízo estimado:** Mais de $2 trilhões globalmente
        
        * **Queda nos mercados:** Principais índices de ações caíram mais de 50%
        
        * **Resgates governamentais:** Centenas de bilhões de dólares em intervenções
        
        * **Desemprego nos EUA:** Aumentou de 5% para mais de 10%
        
        * **Recessão global:** Primeira contração do PIB global desde 1945
        
        * **Instituições falidas:** Lehman Brothers, Washington Mutual, Bear Stearns e outras
        """)
        
        st.markdown('<div class="info-box"><strong>Comece a explorar!</strong><br>Utilize o menu de navegação para acessar as diferentes seções do aplicativo.</div>', unsafe_allow_html=True)

# Conteúdo da página de Linha do Tempo
elif page == "Linha do Tempo":
    st.markdown('<div class="sub-header">Cronologia da Crise</div>', unsafe_allow_html=True)
    
    # Criação das opções de períodos para a linha do tempo
    timeline_periods = [
        "Antecedentes (2001-2006)", 
        "Primeiros Sinais (2006-2007)", 
        "Eclosão da Crise (2007-2008)",
        "Auge da Crise (2008)", 
        "Desdobramentos Globais (2008-2010)",
        "Respostas Políticas (2008-2010)",
        "Consequências (2010-2015)",
        "Legado e Transformações (2015-2023)"
    ]
    
    selected_period = st.selectbox("Selecione um período da linha do tempo:", timeline_periods)
    
    # Dados da linha do tempo para cada período
    timeline_data = {
        "Antecedentes (2001-2006)": [
            {"date": "2001", "description": "Após o estouro da bolha das empresas ponto-com, o Federal Reserve reduz as taxas de juros para próximo de zero para estimular a economia."},
            {"date": "2001-2003", "description": "Baixas taxas de juros estimularam o setor bancário a expandir agressivamente o crédito imobiliário."},
            {"date": "2003-2006", "description": "Proliferação dos empréstimos subprime (alto risco) e instrumentos financeiros complexos como CDOs (Collateralized Debt Obligations) e MBS (Mortgage-Backed Securities)."},
            {"date": "2001-2006", "description": "Os preços dos imóveis sobem em média 85% nos EUA, criando uma bolha especulativa no mercado imobiliário."}
        ],
        "Primeiros Sinais (2006-2007)": [
            {"date": "Meados de 2006", "description": "Os preços dos imóveis atingem o pico e começam a cair. As taxas de inadimplência em empréstimos subprime começam a subir."},
            {"date": "Fev 2007", "description": "O banco HSBC anuncia perdas de US$ 10,5 bilhões relacionadas ao mercado subprime."},
            {"date": "Abr 2007", "description": "New Century Financial, uma das maiores empresas de empréstimos subprime dos EUA, pede falência."},
            {"date": "Jun-Jul 2007", "description": "As agências de classificação de risco (Moody's, S&P) rebaixam centenas de títulos lastreados em hipotecas subprime."},
            {"date": "Ago 2007", "description": "BNP Paribas suspende três fundos devido à impossibilidade de avaliação dos ativos subprime. Este evento é frequentemente considerado o início formal da crise."}
        ],
        "Eclosão da Crise (2007-2008)": [
            {"date": "Set 2007", "description": "Northern Rock, banco britânico, sofre corrida bancária e precisa de resgate do Banco da Inglaterra."},
            {"date": "Out 2007", "description": "UBS e Citigroup anunciam perdas bilionárias relacionadas ao mercado subprime."},
            {"date": "Dez 2007", "description": "Federal Reserve cria a Term Auction Facility (TAF) para fornecer liquidez ao sistema bancário."},
            {"date": "Jan-Fev 2008", "description": "Grandes bancos globais anunciam perdas massivas. O Fed corta as taxas de juros agressivamente."},
            {"date": "Mar 2008", "description": "Bear Stearns, quinto maior banco de investimento dos EUA, é vendido para o JPMorgan Chase com ajuda do Federal Reserve por apenas $10 por ação, totalizando cerca de $1 bilhão, bem abaixo do valor de mercado anterior."}
        ],
        "Auge da Crise (2008)": [
            {"date": "Set 2008 (dia 7)", "description": "O governo americano assume o controle das empresas Fannie Mae e Freddie Mac, gigantes do mercado hipotecário."},
            {"date": "Set 2008 (dia 15)", "description": "Lehman Brothers, quarto maior banco de investimento dos EUA, declara falência. Este é considerado o momento mais dramático da crise."},
            {"date": "Set 2008 (dia 16)", "description": "A seguradora AIG recebe resgate de $180 bilhões do governo americano. O maior resgate da crise"},
            {"date": "Set 2008 (dias 16-20)", "description": "Pânico nos mercados globais. Congelamento do crédito interbancário. Corridas bancárias em várias instituições."},
            {"date": "Out 2008", "description": "Congresso americano aprova o TARP (Troubled Asset Relief Program) de $700 bilhões para comprar ativos tóxicos e recapitalizar bancos."},
            {"date": "Nov-Dez 2008", "description": "Os EUA entram oficialmente em recessão. A taxa de desemprego dispara. Resgates às montadoras americanas."}
        ],
        "Desdobramentos Globais (2008-2010)": [
            {"date": "Out 2008", "description": "Islândia: colapso dos três maiores bancos do país, levando à falência virtual da nação."},
            {"date": "Out-Nov 2008", "description": "Bancos centrais ao redor do mundo coordenam cortes de taxas de juros. FMI resgata países como Hungria, Ucrânia e Paquistão."},
            {"date": "Dez 2008", "description": "China anuncia pacote de estímulo de $586 bilhões. Japão, Reino Unido e União Europeia lançam seus próprios pacotes."},
            {"date": "Jan-Fev 2009", "description": "Economia global entra em recessão sincronizada. O PIB global contrai 0,6% em 2009, a primeira contração desde a Segunda Guerra Mundial."},
            {"date": "Fev 2009", "description": "EUA aprovam o American Recovery and Reinvestment Act de $787 bilhões."},
            {"date": "2009-2010", "description": "Início da crise da dívida soberana europeia, especialmente na Grécia, Irlanda, Portugal, Espanha e Itália."}
        ],
        "Respostas Políticas (2008-2010)": [
            {"date": "Out 2008", "description": "G7 se compromete a tomar 'todas as medidas necessárias' para estabilizar o sistema financeiro."},
            {"date": "Nov 2008", "description": "Primeira cúpula do G20 focada na crise financeira, marcando a ascensão deste grupo como principal fórum econômico global."},
            {"date": "Mar 2009", "description": "Federal Reserve inicia o primeiro programa de Quantitative Easing (QE), comprando $1,25 trilhão em títulos lastreados em hipotecas."},
            {"date": "Abr 2009", "description": "G20 compromete-se a fornecer $1,1 trilhão em recursos para combater a crise global."},
            {"date": "Jul 2010", "description": "Aprovação da Lei Dodd-Frank nos EUA, a maior reforma financeira desde a Grande Depressão."},
            {"date": "Set 2010", "description": "Acordo de Basileia III estabelece novas regras para capital e liquidez bancária a nível global."}
        ],
        "Consequências (2010-2015)": [
            {"date": "2010-2012", "description": "Desaceleração da recuperação econômica global. Persistência de alto desemprego em muitos países desenvolvidos."},
            {"date": "2010-2014", "description": "Crise da dívida europeia se intensifica, forçando resgates da Grécia, Irlanda, Portugal e intervenção no setor bancário espanhol."},
            {"date": "2011-2013", "description": "Protestos sociais como Occupy Wall Street e manifestações contra austeridade na Europa refletem o descontentamento popular."},
            {"date": "2012-2014", "description": "Bancos centrais mantêm políticas monetárias ultrafrouxas. BCE promete fazer 'o que for preciso' para salvar o euro."},
            {"date": "2013-2015", "description": "Recuperação desigual: EUA se recuperam mais rapidamente, enquanto Europa e Japão enfrentam estagnação prolongada. Economias emergentes desaceleram."}
        ],
        "Legado e Transformações (2015-2023)": [
            {"date": "2015-2018", "description": "Federal Reserve inicia normalização monetária gradual. Crescimento global moderado mas estável, com desigualdades crescentes."},
            {"date": "2016-2018", "description": "Ascensão de movimentos políticos populistas e nacionalistas em vários países, parcialmente atribuídos às consequências socioeconômicas da crise."},
            {"date": "2018-2019", "description": "Revisões e flexibilizações de algumas regulações bancárias implementadas pós-crise, especialmente nos EUA."},
            {"date": "2020-2021", "description": "Durante a crise da COVID-19, lições da crise de 2008 permitiram respostas mais rápidas e coordenadas de bancos centrais e governos."},
            {"date": "2022-2023", "description": "Retorno da inflação e aumento das taxas de juros após anos de política monetária expansionista, testando a resiliência do sistema financeiro reformado."}
        ]
    }
    
    # Cores para os diferentes períodos
    period_colors = {
        "Antecedentes (2001-2006)": "#FF9E80",
        "Primeiros Sinais (2006-2007)": "#FFCC80",
        "Eclosão da Crise (2007-2008)": "#FFD180",
        "Auge da Crise (2008)": "#F57C00",
        "Desdobramentos Globais (2008-2010)": "#EF6C00",
        "Respostas Políticas (2008-2010)": "#BF360C",
        "Consequências (2010-2015)": "#B71C1C",
        "Legado e Transformações (2015-2023)": "#880E4F"
    }
    
    # Exibir eventos para o período selecionado
    st.markdown(f'<div style="background-color: {period_colors[selected_period]}22; padding: 1rem; border-radius: 5px; border-left: 5px solid {period_colors[selected_period]}; margin-bottom: 1rem;"><h3 style="margin:0; color: #333;">{selected_period}</h3></div>', unsafe_allow_html=True)
    
    for event in timeline_data[selected_period]:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-date">{event['date']}</div>
            <div class="timeline-description">{event['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Linha do tempo visual simplificada
    st.markdown('<div class="chart-title">Visão Geral da Linha do Tempo</div>', unsafe_allow_html=True)
    

    # Criar tabela de linha do tempo com formatação de cores
    timeline_data = {
        "Período": ["2001-2006", "2006-2007", "2007-2008", "2008 (Set)", "2008-2010", "2008-2010", "2010-2015", "2015-2023"],
        "Fase": ["Formação da Bolha", "Alerta", "Crise Inicial", "Colapso", "Contágio Global", "Intervenção", "Recuperação", "Transformação"],
        "Eventos Chave": [
            "Taxas de juros baixas, desregulamentação, expansão de crédito subprime",
            "Queda nos preços imobiliários, aumento da inadimplência, primeiras falências",
            "Northern Rock, perdas de grandes bancos, venda do Bear Stearns",
            "Lehman Brothers quebra, pânico nos mercados, AIG resgatada, TARP aprovado",
            "Crise na Islândia, pacotes de estímulo globais, recessão sincronizada",
            "Coordenação do G20, programas de QE, reformas regulatórias",
            "Crise da dívida europeia, recuperação lenta, juros baixos prolongados",
            "Normalização monetária, revisão de algumas regulações, lições para a crise da COVID-19"
        ]
    }

    # Cores para cada fase
    colors = [
        "#FF9E80", "#FFCC80", "#FFD180", "#F57C00", 
        "#EF6C00", "#BF360C", "#B71C1C", "#880E4F"
    ]

    # Criar DataFrame
    df_timeline = pd.DataFrame(timeline_data)

    # Gerar HTML para tabela colorida
    html_table = '<table style="width:100%; border-collapse: collapse; margin-bottom: 30px;">'
    html_table += '<tr><th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Período</th>'
    html_table += '<th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Fase</th>'
    html_table += '<th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Eventos Chave</th></tr>'

    for i in range(len(df_timeline)):
        bg_color = f"{colors[i]}33"  # Adiciona transparência à cor
        border_color = colors[i]
        html_table += f'<tr style="background-color: {bg_color}; border-left: 5px solid {border_color};">'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd;">{df_timeline["Período"][i]}</td>'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd; font-weight: bold;">{df_timeline["Fase"][i]}</td>'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd;">{df_timeline["Eventos Chave"][i]}</td>'
        html_table += '</tr>'

    html_table += '</table>'

    # Exibir tabela no Streamlit
    st.markdown(html_table, unsafe_allow_html=True)

    # Adicionar eventos principais em formato de lista
    st.markdown('<div class="chart-title">Eventos Cruciais</div>', unsafe_allow_html=True)

    events = [
        {"data": "Agosto 2007", "evento": "BNP Paribas suspende fundos - Início formal da crise"},
        {"data": "Março 2008", "evento": "Venda emergencial do Bear Stearns para JPMorgan Chase"},
        {"data": "Setembro 2008", "evento": "Falência do Lehman Brothers - Momento mais dramático da crise"},
        {"data": "Outubro 2008", "evento": "Aprovação do TARP ($700 bilhões) para estabilizar o sistema financeiro"},
        {"data": "Março 2009", "evento": "Início do primeiro programa de Quantitative Easing (QE) pelo Federal Reserve"},
        {"data": "Julho 2010", "evento": "Aprovação da Lei Dodd-Frank - Maior reforma financeira desde a Grande Depressão"}
    ]

    for event in events:
        st.markdown(f"""
        <div style="margin-bottom: 10px; padding: 10px; background-color: #f8f9fa; border-left: 3px solid #d63031; border-radius: 3px;">
            <span style="font-weight: bold; color: #d63031;">{event['data']}</span>: {event['evento']}
        </div>
        """, unsafe_allow_html=True)
        
    
    def create_bokeh_timeline():
        # Configurar dados
        phases = ["Formação da Bolha", "Alerta", "Crise Inicial", "Colapso", 
                "Contágio Global", "Intervenção", "Recuperação", "Transformação"]
        
        start_years = [2001, 2006, 2007, 2008, 2008.75, 2008.75, 2010, 2015]
        end_years = [2006, 2007, 2008, 2008.75, 2010, 2010.5, 2015, 2023]
        
        # Eventos importantes
        event_x = [2006.5, 2008.7, 2010, 2010.5]
        event_y = ["Alerta", "Colapso", "Intervenção", "Recuperação"]
        event_text = ["Início do declínio imobiliário", "Falência Lehman Brothers", 
                    "Dodd-Frank & Basileia III", "Crise da dívida europeia"]
        
        # Dados para o gráfico
        source = ColumnDataSource(data=dict(
            phase=phases,
            start=start_years,
            end=end_years,
            duration=[e-s for s, e in zip(start_years, end_years)],
            color=Spectral8[::-1]  # Inverte a paleta para cores semelhantes
        ))
        
        # Dados para eventos
        event_source = ColumnDataSource(data=dict(
            x=event_x,
            y=event_y,
            text=event_text
        ))
        
        # Criar figura
        p = figure(
            y_range=phases,
            x_range=(2000, 2024),
            height=500,
            title="Linha do Tempo da Crise Subprime",
            toolbar_location=None,
            sizing_mode="stretch_width"
        )
        
        # Adicionar barras horizontais
        p.hbar(
            y="phase",
            left="start",
            right="end",
            height=0.8,
            source=source,
            color="color",
            line_color="white",
            line_width=2
        )
        
        # Adicionar rótulos dentro das barras
        labels = LabelSet(
            x='start',
            y='phase',
            text='phase',
            source=source,
            text_align='left',
            x_offset=5,
            y_offset=0,
            text_font_size='10pt'
        )
        p.add_layout(labels)
        
        # Adicionar círculos para eventos
        p.circle(
            x='x',
            y='y',
            size=10,
            source=event_source,
            color='black',
            alpha=0.8
        )
        
        # Adicionar rótulos para eventos
        event_labels = LabelSet(
            x='x',
            y='y',
            text='text',
            source=event_source,
            text_align='center',
            x_offset=0,
            y_offset=-20,
            text_font_size='9pt',
            text_color='#333333',
            background_fill_color='white',
            background_fill_alpha=0.7,
            border_line_color='black',
            border_line_alpha=0.2
        )
        p.add_layout(event_labels)
        
        # Estilizar o gráfico
        p.xaxis.axis_label = "Ano"
        p.yaxis.axis_label = ""
        p.outline_line_color = None
        p.grid.grid_line_color = None
        
        # Configurar ticks de ano
        p.xaxis.ticker = list(range(2001, 2024, 2))
        
        # Retornar HTML
        return file_html(p, CDN)

    # Dentro da seção da linha do tempo, substitua o código do gráfico pelo seguinte:
    html = create_bokeh_timeline()
    components.html(html, height=550)

    # Não se esqueça de adicionar bokeh às dependências
            
    
# Conteúdo da página de Bolha Imobiliária
elif page == "Bolha Imobiliária":
    st.markdown('<div class="sub-header">Evolução da Bolha Imobiliária nos EUA</div>', unsafe_allow_html=True)
    
    # Dados do Índice Case-Shiller S&P/Case-Shiller 20-City Composite Home Price Index
    dates = [2000, 2000.5, 2001, 2001.5, 2002, 2002.5, 2003, 2003.5, 2004, 2004.5, 2005, 2005.5, 2006, 2006.5, 2007, 2007.5, 2008, 2008.5, 2008.75, 2009, 2009.5, 2010, 2010.5, 2011, 2011.5, 2012, 2012.5]
    values = [100.0, 105.2, 110.8, 116.5, 121.9, 129.6, 138.1, 146.7, 157.6, 170.9, 181.5, 198.6, 204.8, 206.2, 198.4, 189.2, 173.5, 162.8, 158.1, 147.8, 143.2, 145.6, 147.8, 141.9, 142.2, 140.6, 145.3]
    
    # Criar DataFrame
    df_housing = pd.DataFrame({
        'Data': dates,
        'Índice': values
    })
    
    # Adicionar coluna para fases
    conditions = [
        (df_housing['Data'] <= 2006.5),
        (df_housing['Data'] > 2006.5) & (df_housing['Data'] <= 2008.75),
        (df_housing['Data'] > 2008.75)
    ]
    phases = ['Formação da Bolha', 'Estouro da Bolha', 'Crise e Recuperação Lenta']
    colors = ['rgba(255, 200, 0, 0.2)', 'rgba(255, 100, 0, 0.2)', 'rgba(255, 0, 0, 0.2)']
    
    df_housing['Fase'] = np.select(conditions, phases)
    
    # Eventos importantes
    events = [
        {'data': 2006.5, 'evento': 'Pico da bolha', 'valor': 206.2},
        {'data': 2007.5, 'evento': 'Crise subprime começa', 'valor': 189.2},
        {'data': 2008.75, 'evento': 'Quebra do Lehman Brothers', 'valor': 158.1}
    ]
    
    # Criação do gráfico com Plotly
    fig = px.line(df_housing, x='Data', y='Índice', title='')
    
    # Adicionar áreas sombreadas para as fases
    for phase, color in zip(phases, colors):
        phase_data = df_housing[df_housing['Fase'] == phase]
        if not phase_data.empty:
            x_range = [phase_data['Data'].min(), phase_data['Data'].max()]
            y_range = [df_housing['Índice'].min() * 0.95, df_housing['Índice'].max() * 1.05]
            
            fig.add_shape(
                type="rect",
                x0=x_range[0],
                x1=x_range[1],
                y0=y_range[0],
                y1=y_range[1],
                fillcolor=color,
                opacity=0.8,
                layer="below",
                line_width=0,
            )
    
    # Adicionar linhas verticais e anotações para eventos importantes
    for event in events:
        fig.add_vline(x=event['data'], line_dash="dash", line_color="red", line_width=1)
        fig.add_annotation(
            x=event['data'],
            y=event['valor'],
            text=event['evento'],
            showarrow=True,
            arrowhead=1,
            ax=0,
            ay=-40
        )
    
    # Atualizar layout
    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Índice Case-Shiller (2000=100)",
        height=600,
        hovermode="x unified",
        legend_title="Fase",
        xaxis=dict(
            tickmode='array',
            tickvals=[2000, 2002, 2004, 2006, 2007, 2008, 2009, 2010, 2012],
            ticktext=['2000', '2002', '2004', '2006', '2007', '2008', '2009', '2010', '2012']
        ),
        shapes=[
            # Linha horizontal para o nível de 2000
            dict(
                type="line",
                x0=2000,
                x1=2012.5,
                y0=100,
                y1=100,
                line=dict(color="gray", width=1, dash="dot"),
            )
        ]
    )
    
    fig.update_traces(line=dict(color='#FF5722', width=3), hovertemplate='Ano: %{x}<br>Índice: %{y:.1f}')
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Adicionar explicação
    st.markdown("""
    <div class="info-box">
    <h3>Anatomia da Bolha Imobiliária</h3>
    <p>O gráfico acima mostra a evolução do Índice Case-Shiller, que mede os preços de imóveis residenciais em 20 grandes áreas metropolitanas nos EUA. Observe as três fases distintas:</p>
    <ol>
        <li><strong>Formação da Bolha (2000-2006):</strong> Preços subiram mais de 100% em apenas 6 anos, impulsionados por taxas de juros baixas, regulação frouxa e inovações financeiras que expandiram o crédito imobiliário.</li>
        <li><strong>Estouro da Bolha (2006-2008):</strong> Quando as taxas de juros subiram e as taxas de inadimplência aumentaram, os preços começaram a cair, criando um ciclo vicioso de execuções hipotecárias e mais quedas nos preços.</li>
        <li><strong>Crise e Recuperação Lenta (2008-2012):</strong> Após o colapso do Lehman Brothers, a crise se aprofundou e os preços continuaram caindo, com uma recuperação muito lenta que só começou em 2012.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Adicionar fatores que contribuíram para a bolha imobiliária
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-title">Fatores que Contribuíram para a Bolha</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Política monetária frouxa**: Taxas de juros baixas após a crise das empresas ponto-com
        - **Política governamental**: Incentivos à expansão da propriedade imobiliária
        - **Inovação financeira**: Securitização e produtos estruturados complexos
        - **Regulação inadequada**: Supervisão fraca do mercado de hipotecas
        - **Incentivos distorcidos**: Originadores de hipotecas sem responsabilidade pelo risco
        - **Avaliações otimistas**: Expectativa de valorização contínua dos imóveis
        - **Classificações de risco falhas**: Agências de rating atribuindo AAA a produtos tóxicos
        """)
    
    with col2:
        st.markdown('<div class="chart-title">Taxas de Hipotecas Subprime (2000-2008)</div>', unsafe_allow_html=True)
        
        # Dados fictícios para ilustrar o crescimento das hipotecas subprime
        subprime_years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
        subprime_share = [8, 9, 12, 14, 18, 22, 23.5, 21, 15]
        
        # Criar gráfico de barras
        fig_subprime = px.bar(
            x=subprime_years, 
            y=subprime_share,
            labels={'x': 'Ano', 'y': '% do Mercado Hipotecário'},
            title=''
        )
        
        fig_subprime.update_traces(marker_color=['#90CAF9', '#90CAF9', '#90CAF9', '#90CAF9', '#FFAB91', '#FF8A65', '#FF7043', '#F4511E', '#D84315'])
        
        fig_subprime.update_layout(
            height=300,
            xaxis_title="Ano",
            yaxis_title="% do Mercado Hipotecário",
            hovermode="x"
        )
        
        st.plotly_chart(fig_subprime, use_container_width=True)
        
        st.markdown("""
        <div style="font-size: 0.8rem; color: #666; text-align: center; margin-top: -15px;">
        Participação dos empréstimos subprime no mercado hipotecário dos EUA.
        </div>
        """, unsafe_allow_html=True)

# Conteúdo da página de Impacto Global
elif page == "Impacto Global":
    st.markdown('<div class="sub-header">Impactos Econômicos Globais da Crise</div>', unsafe_allow_html=True)
    
    # Oferece opções para diferentes visualizações de impacto
    impact_metric = st.radio(
        "Selecione uma métrica de impacto:",
        ["Crescimento do PIB", "Desemprego", "Dívida Pública"],
        horizontal=True
    )
    
    if impact_metric == "Crescimento do PIB":
        # Dados de crescimento do PIB (variação % anual)
        gdp_data = {
            'País': ['EUA', 'Reino Unido', 'Japão', 'Alemanha', 'França', 'Brasil', 'China', 'Índia', 'Rússia'],
            '2007': [1.9, 2.7, 1.7, 3.0, 2.4, 6.1, 14.2, 9.8, 8.5],
            '2008': [-0.1, -0.3, -1.1, 0.8, 0.3, 5.1, 9.7, 3.9, 5.2],
            '2009': [-2.5, -4.2, -5.4, -5.7, -2.9, -0.1, 9.4, 8.5, -7.8]
        }
        
        df_gdp = pd.DataFrame(gdp_data)
        
        # Reorganizar os dados para o formato "long" para Plotly
        df_gdp_long = pd.melt(df_gdp, id_vars=['País'], var_name='Ano', value_name='Crescimento do PIB (%)')
        
        # Criar gráfico de barras
        fig = px.bar(
            df_gdp_long, 
            x='País', 
            y='Crescimento do PIB (%)', 
            color='Ano',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2008': '#FFC107', '2009': '#FF5722'},
            title='Impacto no Crescimento Econômico entre 2007-2009',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="Crescimento do PIB (%)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impacto no Crescimento Econômico</h3>
        <p>A crise causou uma forte contração econômica global:</p>
        <ul>
            <li><strong>Economias avançadas:</strong> Foram as mais atingidas, com contrações severas em 2009.</li>
            <li><strong>Rússia:</strong> Entre as economias emergentes, sofreu a maior contração devido à dependência de commodities.</li>
            <li><strong>China e Índia:</strong> Mantiveram crescimento positivo, embora desacelerado, em parte devido aos grandes pacotes de estímulo.</li>
            <li><strong>Brasil:</strong> Experimentou uma breve contração seguida de rápida recuperação em 2010.</li>
        </ul>
        <p>Esta foi a primeira recessão global sincronizada desde a Segunda Guerra Mundial.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif impact_metric == "Desemprego":
        # Dados de desemprego (% da força de trabalho)
        unemployment_data = {
            'País': ['EUA', 'Reino Unido', 'Japão', 'Alemanha', 'França', 'Espanha', 'Grécia'],
            '2007': [4.6, 5.3, 3.9, 8.6, 8.0, 8.2, 8.4],
            '2008': [5.8, 5.6, 4.0, 7.5, 7.4, 11.3, 7.8],
            '2009': [9.3, 7.6, 5.1, 7.8, 9.1, 17.9, 9.6],
            '2010': [9.6, 7.8, 5.1, 7.1, 9.3, 19.9, 12.7]
        }
        
        df_unemployment = pd.DataFrame(unemployment_data)
        
        # Reorganizar os dados para o formato "long" para Plotly
        df_unemp_long = pd.melt(df_unemployment, id_vars=['País'], var_name='Ano', value_name='Taxa de Desemprego (%)')
        
        # Criar gráfico de barras
        fig = px.bar(
            df_unemp_long, 
            x='País', 
            y='Taxa de Desemprego (%)', 
            color='Ano',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2008': '#FFC107', '2009': '#FF5722', '2010': '#9C27B0'},
            title='Evolução da Taxa de Desemprego entre 2007-2010',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="Taxa de Desemprego (%)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impacto no Mercado de Trabalho</h3>
        <p>A crise causou um aumento significativo do desemprego em muitos países:</p>
        <ul>
            <li><strong>EUA:</strong> A taxa de desemprego dobrou, passando de 4,6% para mais de 9%.</li>
            <li><strong>Europa do Sul:</strong> Espanha e Grécia sofreram os impactos mais graves, com taxas de desemprego chegando a quase 20% na Espanha.</li>
            <li><strong>Alemanha:</strong> Experienciou menor impacto devido a políticas de trabalho flexíveis (Kurzarbeit) que permitiram redução de horas em vez de demissões.</li>
            <li><strong>Recuperação lenta:</strong> Na maioria dos países, o desemprego continuou subindo mesmo após o PIB começar a se recuperar (fenômeno conhecido como "jobless recovery").</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Dívida Pública
        # Dados da dívida pública (% do PIB)
        debt_data = {
            'País': ['EUA', 'Reino Unido', 'Japão', 'Alemanha', 'França', 'Itália', 'Grécia', 'Espanha', 'Irlanda'],
            '2007': [64.0, 43.5, 183.0, 63.7, 64.2, 103.1, 107.4, 36.3, 24.8],
            '2010': [91.4, 75.6, 215.8, 82.5, 82.3, 119.1, 146.2, 60.1, 86.8],
            'Aumento': [27.4, 32.1, 32.8, 18.8, 18.1, 16.0, 38.8, 23.8, 62.0]
        }
        
        df_debt = pd.DataFrame(debt_data)
        
        # Reorganizar os dados para o formato "long" para Plotly
        df_debt_long = pd.melt(df_debt, id_vars=['País'], var_name='Período', value_name='Dívida (% do PIB)')
        
        # Criar gráfico de barras
        fig = px.bar(
            df_debt_long, 
            x='País', 
            y='Dívida (% do PIB)', 
            color='Período',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2010': '#FF5722', 'Aumento': 'orange'},
            title='Aumento da Dívida Pública entre 2007-2010 devido aos Resgates e Estímulos Econômicos',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="Dívida Pública (% do PIB)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impacto nas Finanças Públicas</h3>
        <p>A crise levou a um aumento dramático das dívidas públicas devido a:</p>
        <ul>
            <li><strong>Resgates bancários:</strong> Governos injetaram centenas de bilhões para salvar instituições financeiras.</li>
            <li><strong>Pacotes de estímulo fiscal:</strong> Gastos públicos para compensar a queda na demanda privada.</li>
            <li><strong>Receitas fiscais reduzidas:</strong> Devido à contração econômica e aumento do desemprego.</li>
            <li><strong>Irlanda:</strong> Registrou o maior aumento relativo, com sua dívida mais que triplicando em três anos.</li>
            <li><strong>Grécia:</strong> A alta dívida pré-crise combinada com o aumento levou à crise da dívida soberana europeia.</li>
        </ul>
        <p>Este aumento da dívida pública levou posteriormente a políticas de austeridade em muitos países, especialmente na Europa.</p>
        </div>
        """, unsafe_allow_html=True)

# Conteúdo da página de Securitização
elif page == "Securitização":
    st.markdown('<div class="sub-header">Inovações Financeiras e Securitização</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    A securitização e as inovações financeiras complexas foram elementos centrais na crise subprime. 
    Este diagrama ilustra como os empréstimos imobiliários de alto risco foram transformados em produtos 
    financeiros complexos e distribuídos pelo sistema financeiro global.
    </div>
    """, unsafe_allow_html=True)
    
    # Criar diagrama de securitização com networkx e matplotlib
    st.markdown('<div class="chart-title">Fluxo do Processo de Securitização</div>', unsafe_allow_html=True)
    
    # Criar um diagrama simplificado do processo de securitização
    G = nx.DiGraph()
    
    # Adicionar nós para os diferentes participantes e instrumentos
    nodes = {
        "Famílias": {"type": "participant", "level": 0, "pos": (0, 4.6)},
        "Bcos Originadores": {"type": "bank", "level": 1, "pos": (1.8, 4)},
        "Hipotecas Prime": {"type": "asset", "level": 1.5, "pos": (4, 5)},
        "Hipotecas Subprime": {"type": "asset", "level": 1.5, "pos": (4, 3)},
        "Bcos de Investimento": {"type": "bank", "level": 2, "pos": (6, 4)},
        "SPV": {"type": "special", "level": 3, "pos": (8, 4.7)},
        "SIV": {"type": "special", "level": 3, "pos": (8, 3.3)},
        "MBS": {"type": "asset", "level": 4, "pos": (10, 4)},
        "CDO": {"type": "asset", "level": 5, "pos": (12, 4)},
        "Bcos Europa": {"type": "bank", "level": 6.3, "pos": (15, 4)},
        "Tranche AAA": {"type": "asset", "level": 6, "pos": (13, 5)},
        "Tranche BBB": {"type": "asset", "level": 6, "pos": (13.15, 3.25)},
        "Fundos de Pensão": {"type": "investor", "level": 7, "pos": (17, 5)},
        "Hedge Funds": {"type": "investor", "level": 7, "pos": (16.85, 3.25)},
        "CDS": {"type": "risk", "level": 5.5, "pos": (12, 2)},
        "Sistema Global": {"type": "investor", "level": 8, "pos": (18, 4)},
    }
    
    # Adicionar nós ao grafo
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)
    
    # Adicionar arestas
    edges = [
        ("Famílias", "Bcos Originadores", "Tomam empréstimos"),
        ("Bcos Originadores", "Hipotecas Prime", "Originam"),
        ("Bcos Originadores", "Hipotecas Subprime", "Originam"),
        ("Bcos Originadores", "Bcos de Investimento", "Vendem hipotecas"),
        ("Hipotecas Prime", "Bcos de Investimento", ""),
        ("Hipotecas Subprime", "Bcos de Investimento", ""),
        ("Bcos de Investimento", "SPV", "Criam"),
        ("Bcos de Investimento", "SIV", "Mantém fora do balanço"),
        ("SPV", "MBS", "Emitem"),
        ("MBS", "CDO", "Estruturam"),
        ("CDO", "Tranche AAA", "Segmentam por risco"),
        ("CDO", "Bcos Europa", "Compram"),
        ("CDO", "Tranche BBB", "Segmentam por risco"),
        ("CDO", "CDS", "Proteção contra default"),
        ("Tranche AAA", "Fundos de Pensão", "Compram"),
        ("Tranche BBB", "Hedge Funds", "Compram"),
        ("Bcos Europa", "Sistema Global", "Propagação do risco"),
        ("Fundos de Pensão", "Sistema Global", "Propagação do risco"),
        ("Hedge Funds", "Sistema Global", "Propagação do risco"),
        ("CDS", "Sistema Global", "Interconexão")
    ]
    
    for u, v, label in edges:
        G.add_edge(u, v, label=label)
    
    # Criar plot
    plt.figure(figsize=(14, 8))
    pos = nx.get_node_attributes(G, 'pos')
    
    # Definir cores com base no tipo de nó
    color_map = []
    for node in G:
        node_type = G.nodes[node]['type']
        if node_type == 'participant':
            color_map.append('#E1BEE7')  # Lilás claro
        elif node_type == 'bank':
            color_map.append('#BBDEFB')  # Azul claro
        elif node_type == 'asset':
            color_map.append('#FFF9C4')  # Amarelo claro
        elif node_type == 'investor':
            color_map.append('#C8E6C9')  # Verde claro
        elif node_type == 'risk':
            color_map.append('#FFCDD2')  # Vermelho claro
        elif node_type == 'special':
            color_map.append('#D1C4E9')  # Roxo claro
    
    # Desenhar nós e bordas
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=color_map, alpha=0.8, edgecolors='gray', linewidths=1)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=15, arrowstyle='->')
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
    
    # Adicionar labels às bordas
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
    
    # Adicionar legenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#E1BEE7', markersize=10, label='Participantes'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#BBDEFB', markersize=10, label='Bancos'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFF9C4', markersize=10, label='Ativos'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#C8E6C9', markersize=10, label='Investidores'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFCDD2', markersize=10, label='Instrumentos de Risco'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#D1C4E9', markersize=10, label='Veículos Especiais')
    ]
    
    plt.legend(handles=legend_elements, loc='lower right')
    plt.axis('off')
    plt.tight_layout()
    
    # Exibir o gráfico no Streamlit
    st.pyplot(plt)
    
    # Explicações sobre os instrumentos financeiros
    st.markdown('<div class="sub-header">Instrumentos Financeiros Complexos</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### MBS (Mortgage-Backed Securities)
        Títulos lastreados em hipotecas, que agrupam centenas ou milhares de empréstimos imobiliários em um único produto financeiro. Os investidores que compram MBS recebem pagamentos baseados no fluxo de caixa dos empréstimos subjacentes.
        
        ### CDO (Collateralized Debt Obligations)
        Produtos estruturados que agrupam diversos ativos geradores de fluxo de caixa (incluindo MBS) e os dividem em "tranches" com diferentes níveis de risco e retorno. As tranches superiores (AAA) tinham prioridade no recebimento dos fluxos de caixa, enquanto as inferiores absorviam as primeiras perdas.
        
        ### CDO² (CDO de CDOs)
        Uma camada adicional de complexidade: CDOs compostos por tranches de outros CDOs. Esta resecuritização tornava extremamente difícil avaliar os riscos reais dos ativos subjacentes.
        """)
    
    with col2:
        st.markdown("""
        ### CDS (Credit Default Swaps)
        Contratos de seguro que protegiam contra o risco de inadimplência. O comprador pagava um prêmio periódico ao vendedor, que garantia compensação em caso de "evento de crédito" (como default). Foram amplamente utilizados para especular, não apenas para se proteger contra riscos.
        
        ### SIV (Structured Investment Vehicles)
        Entidades criadas por bancos para manter ativos fora do balanço. Os SIVs emitiam papel comercial de curto prazo para financiar a compra de ativos de longo prazo como MBS, criando um descasamento de prazos que se mostrou fatal durante a crise.
        
        ### SPV (Special Purpose Vehicles)
        Entidades legais criadas especificamente para isolar riscos financeiros. Eram fundamentais no processo de securitização, permitindo que os bancos transferissem ativos e seus riscos associados para fora de seus balanços.
        """)
    
    st.markdown("""
    <div class="info-box">
    <h3>Problemas Fundamentais do Modelo de Securitização</h3>
    <ul>
        <li><strong>Incentivos distorcidos:</strong> O modelo "originar para distribuir" removeu o incentivo para uma avaliação rigorosa do risco de crédito.</li>
        <li><strong>Opacidade e complexidade:</strong> Investidores não conseguiam avaliar adequadamente os riscos dos produtos estruturados que compravam.</li>
        <li><strong>Falhas nas agências de rating:</strong> Conflitos de interesse levaram à classificação excessivamente otimista de produtos tóxicos.</li>
        <li><strong>Concentração oculta de riscos:</strong> Bancos mantiveram exposição significativa através de linhas de crédito e garantias implícitas.</li>
        <li><strong>Alavancagem excessiva:</strong> A securitização permitiu que instituições contornassem requisitos de capital e aumentassem drasticamente sua alavancagem.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Conteúdo da página de Respostas Regulatórias
elif page == "Respostas Regulatórias":
    st.markdown('<div class="sub-header">Respostas Regulatórias à Crise</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    Após a crise, governos e reguladores implementaram uma série de reformas para corrigir as falhas 
    reveladas pela crise e fortalecer o sistema financeiro. As tabelas abaixo resumem as principais 
    medidas por região.
    </div>
    """, unsafe_allow_html=True)
    
    # Tabelas de respostas regulatórias
    region = st.radio(
        "Selecione uma região:",
        ["Estados Unidos", "União Europeia", "Internacional (Basileia)"],
        horizontal=True
    )
    
    if region == "Estados Unidos":
        st.markdown("""
        ## Principais Medidas Regulatórias nos Estados Unidos
        
        | Medida | Ano | Objetivos Principais | Impactos |
        |--------|-----|----------------------|----------|
        | **Lei Dodd-Frank** | 2010 | • Maior supervisão de instituições sistemicamente importantes;  • Criação do Financial Stability Oversight Council;  • Regulação de derivativos de balcão;  • Criação do Consumer Financial Protection Bureau;  • Regra Volcker (limita proprietary trading) | • Aumento de requisitos de capital para bancos;  • Maior transparência no mercado de derivativos;  • Restrições às atividades especulativas dos bancos;  • Proteção aprimorada ao consumidor financeiro |
        | **Teste de Estresse** | 2009-atual | • Avaliar capacidade dos bancos de resistir a cenários adversos;  • Identificar vulnerabilidades sistêmicas | • Fortalecimento da resiliência bancária;  • Maior transparência sobre riscos;  • Base para exigências de capital adicionais |
        | **Regras de Liquidez** | 2013-2015 | • Índice de Cobertura de Liquidez (LCR);  • Índice de Financiamento Estável Líquido (NSFR) | • Redução da vulnerabilidade a choques de liquidez;  • Menor dependência de financiamento de curto prazo |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Foco da Abordagem dos EUA</h3>
        <p>A resposta regulatória dos EUA focou principalmente em:</p>
        <ul>
            <li>Maior proteção ao consumidor financeiro</li>
            <li>Supervisão reforçada das instituições sistemicamente importantes</li>
            <li>Maior transparência e regulamentação dos mercados de derivativos</li>
            <li>Limites à tomada de riscos pelos bancos</li>
        </ul>
        <p>Contudo, desde 2018, algumas partes da Lei Dodd-Frank foram relaxadas, especialmente para bancos de médio porte.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif region == "União Europeia":
        st.markdown("""
        ## Principais Medidas Regulatórias na União Europeia
        
        | Medida | Ano | Objetivos Principais | Impactos |
        |--------|-----|----------------------|----------|
        | **União Bancária** | 2012-2014 | • Mecanismo Único de Supervisão (SSM);  • Mecanismo Único de Resolução (SRM);  • Sistema de Garantia de Depósitos | • Supervisão centralizada dos maiores bancos europeus;  • Redução do vínculo banco-soberano;  • Processo de resolução bancária harmonizado |
        | **CRD IV/CRR** | 2013 | • Implementação do Basileia III na Europa;  • Requisitos de capital mais rigorosos;  • Limitação dos bônus bancários | • Aumento do capital regulatório;  • Introdução de buffer de conservação e contracíclico;  • Controles sobre remuneração do setor financeiro |
        | **MiFID II/MiFIR** | 2018 | • Maior transparência nos mercados financeiros;  • Proteção ao investidor aprimorada;  • Regulação de trading de alta frequência | • Regras mais rígidas de execução de ordens;  • Melhoria na formação de preços;  • Redução de conflitos de interesse |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Foco da Abordagem Europeia</h3>
        <p>A resposta regulatória da UE focou principalmente em:</p>
        <ul>
            <li>Criação de uma arquitetura institucional supranacional para supervisão bancária</li>
            <li>Quebra do círculo vicioso entre bancos e dívidas soberanas</li>
            <li>Harmonização das regras em todo o mercado único</li>
            <li>Controle mais rígido sobre a remuneração no setor financeiro</li>
        </ul>
        <p>A implementação completa da União Bancária, contudo, permanece incompleta, com o Sistema Europeu de Seguro de Depósitos ainda em discussão.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Internacional (Basileia)
        st.markdown("""
        ## Principais Medidas Regulatórias Internacionais (Basileia)
        
        | Medida | Ano | Objetivos Principais | Impactos |
        |--------|-----|----------------------|----------|
        | **Basileia III** | 2010-2022 | • Aumento na qualidade e quantidade do capital;  • Introdução de buffer contracíclico;  • Limitação da alavancagem;  • Padrões de liquidez globais | • Capital Tier 1 aumentado de 4% para 6%;  • Introdução do índice de alavancagem de 3%;  • Padrões de gestão de risco aprimorados;  • Sistema financeiro global mais resiliente |
        | **G-SIBs/D-SIBs** | 2011-2012 | • Identificação de bancos sistêmicos globais e domésticos;  • Requisitos adicionais para instituições críticas | • Capital adicional para bancos sistemicamente importantes;  • Planos de recuperação e resolução;  • Supervisão mais intensa |
        | **FSB** | 2009 | • Coordenação internacional de regulação financeira;  • Monitoramento de riscos sistêmicos;  • Implementação de reformas do G20 | • Maior coordenação regulatória global;  • Revisão por pares das reformas nacionais;  • Padrões globais para instituições financeiras |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Foco da Abordagem Internacional</h3>
        <p>A resposta regulatória internacional focou principalmente em:</p>
        <ul>
            <li>Fortalecimento da resiliência dos bancos individuais</li>
            <li>Redução do risco sistêmico no sistema bancário global</li>
            <li>Melhoria da cooperação e coordenação entre reguladores nacionais</li>
            <li>Padrões mínimos globais para capital, liquidez e gestão de risco</li>
        </ul>
        <p>Embora Basileia III represente um fortalecimento significativo em relação aos acordos anteriores, sua implementação varia entre jurisdições e os prazos foram estendidos várias vezes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Evolução dos requisitos de capital
    st.markdown('<div class="chart-title">Evolução dos Requisitos de Capital Bancário</div>', unsafe_allow_html=True)
    
    # Dados para o gráfico de evolução dos requisitos de capital
    basel_years = ["Basileia I\n(1988)", "Basileia II\n(2004)", "Basileia III\n(2010)", "Basileia III\n(Implementação Final)"]
    total_capital = [8, 8, 10.5, 13]
    tier1_capital = [4, 4, 6, 8.5]
    core_tier1 = [0, 2, 4.5, 7]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[8, 8, 10.5, 13],
        name='Capital Total',
        marker_color='#90CAF9'
    ))
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[4, 4, 6, 8.5],
        name='Capital Tier 1',
        marker_color='#42A5F5'
    ))
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[0, 2, 4.5, 7],
        name='Capital Core Tier 1',
        marker_color='#1976D2'
    ))
    
    fig.update_layout(
        barmode='group',
        xaxis=dict(title='Acordo de Basileia'),
        yaxis=dict(title='% dos Ativos Ponderados pelo Risco', range=[0, 14]),
        legend=dict(x=0.1, y=1.15, orientation='h'),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div style="font-size: 0.8rem; color: #666; text-align: center; margin-top: -20px;">
    Evolução dos requisitos mínimos de capital ao longo dos acordos de Basileia. Os requisitos do Basileia III incluem o buffer de conservação de capital.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>Eficácia das Reformas Regulatórias</h3>
    <p>Mais de uma década após a crise, os debates sobre a eficácia das reformas regulatórias continuam:</p>
    <ul>
        <li><strong>Pontos positivos:</strong> Sistema bancário com mais capital e liquidez, maior transparência nos mercados de derivativos, melhor supervisão de instituições sistemicamente importantes.</li>
        <li><strong>Questões pendentes:</strong> "Too big to fail" não foi totalmente resolvido, shadow banking continua crescendo, complexidade regulatória aumentou substancialmente.</li>
        <li><strong>Novos desafios:</strong> Fintech, criptomoedas e finanças descentralizadas estão criando novos riscos potenciais fora do perímetro regulatório tradicional.</li>
    </ul>
    <p>A crise da COVID-19 em 2020 serviu como primeiro grande teste para o sistema financeiro reformado, que demonstrou maior resiliência do que em 2008, mas ainda com necessidade de suporte significativo dos bancos centrais.</p>
    </div>
    """, unsafe_allow_html=True)

# Conteúdo da página de Lições Aprendidas
elif page == "Lições Aprendidas":
    st.markdown('<div class="sub-header">Lições da Crise Subprime</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    A crise subprime ofereceu lições valiosas sobre o funcionamento dos mercados financeiros, 
    a gestão de risco, a regulação financeira e as políticas macroeconômicas. Algumas dessas 
    lições foram implementadas, enquanto outras continuam sendo debatidas.
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs para diferentes categorias de lições
    lesson_tabs = st.tabs([
        "Falhas de Mercado", 
        "Gestão de Risco", 
        "Governança e Supervisão", 
        "Perspectivas Econômicas",
        "Desafios Persistentes"
    ])
    
    with lesson_tabs[0]:  # Falhas de Mercado
        st.markdown("""
        <div class="tab-content">
        <h3>Informação Assimétrica</h3>
        <ul>
            <li><strong>Problema:</strong> Investidores confiaram excessivamente nas agências de rating sem entender os produtos financeiros complexos</li>
            <li><strong>Lição:</strong> A opacidade e complexidade em produtos financeiros podem esconder riscos sistêmicos</li>
            <li><strong>Medida corretiva:</strong> Maior transparência e divulgação obrigatória de riscos</li>
        </ul>

        <h3>Incentivos Distorcidos</h3>
        <ul>
            <li><strong>Problema:</strong> Modelo "originar para distribuir" removeu incentivo para avaliação adequada de risco</li>
            <li><strong>Lição:</strong> Estruturas de compensação e incentivos devem estar alinhados com estabilidade de longo prazo</li>
            <li><strong>Medida corretiva:</strong> Requisitos de retenção de risco ("skin in the game") para originadores</li>
        </ul>

        <h3>Regulação Inadequada</h3>
        <ul>
            <li><strong>Problema:</strong> Sistema bancário paralelo (shadow banking) operava com supervisão limitada</li>
            <li><strong>Lição:</strong> Arbitragem regulatória cria vulnerabilidades sistêmicas</li>
            <li><strong>Medida corretiva:</strong> Supervisão abrangente baseada em atividades, não apenas em entidades</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[1]:  # Gestão de Risco
        st.markdown("""
        <div class="tab-content">
        <h3>Risco de Cauda</h3>
        <ul>
            <li><strong>Problema:</strong> Modelos subestimaram eventos extremos e correlações em tempos de crise</li>
            <li><strong>Lição:</strong> "Cisnes negros" ocorrem com mais frequência do que os modelos sugerem</li>
            <li><strong>Medida corretiva:</strong> Testes de estresse mais rigorosos e consideração de cenários extremos</li>
        </ul>

        <h3>Correlações Dinâmicas</h3>
        <ul>
            <li><strong>Problema:</strong> Diversificação falhou quando correlações entre ativos aumentaram durante a crise</li>
            <li><strong>Lição:</strong> Benefícios da diversificação podem desaparecer quando mais necessários</li>
            <li><strong>Medida corretiva:</strong> Modelos de risco devem considerar correlações dinâmicas e não apenas dados históricos</li>
        </ul>

        <h3>Risco de Liquidez</h3>
        <ul>
            <li><strong>Problema:</strong> Instituições dependiam excessivamente de financiamento de curto prazo</li>
            <li><strong>Lição:</strong> Descasamento de prazos pode rapidamente se tornar fatal em períodos de estresse</li>
            <li><strong>Medida corretiva:</strong> Padrões de liquidez (LCR e NSFR) e gestão de liquidez aprimorada</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[2]:  # Governança e Supervisão
        st.markdown("""
        <div class="tab-content">
        <h3>Visão Sistêmica</h3>
        <ul>
            <li><strong>Problema:</strong> Reguladores focavam em instituições individuais, não no sistema como um todo</li>
            <li><strong>Lição:</strong> Estabilidade de instituições individuais não garante estabilidade sistêmica</li>
            <li><strong>Medida corretiva:</strong> Criação de órgãos de supervisão macroprudencial (ex: FSOC nos EUA)</li>
        </ul>

        <h3>Too Big To Fail</h3>
        <ul>
            <li><strong>Problema:</strong> Instituições grandes demais para quebrar criaram risco moral</li>
            <li><strong>Lição:</strong> O custo de resgates públicos é inaceitavelmente alto</li>
            <li><strong>Medida corretiva:</strong> Requisitos adicionais para bancos sistêmicos e regimes de resolução</li>
        </ul>

        <h3>Coordenação Internacional</h3>
        <ul>
            <li><strong>Problema:</strong> Resposta fragmentada à crise global</li>
            <li><strong>Lição:</strong> Mercados financeiros são globais, exigindo coordenação regulatória internacional</li>
            <li><strong>Medida corretiva:</strong> Fortalecimento do FSB e implementação global de padrões de Basileia</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[3]:  # Perspectivas Econômicas
        st.markdown("""
        <div class="tab-content">
        <h3>Bolhas de Ativos</h3>
        <ul>
            <li><strong>Problema:</strong> Políticas monetárias frouxas contribuíram para a bolha imobiliária</li>
            <li><strong>Lição:</strong> Política monetária deve considerar estabilidade financeira, não apenas inflação</li>
            <li><strong>Medida corretiva:</strong> Ferramentas macroprudenciais para conter crescimento insustentável de crédito</li>
        </ul>

        <h3>Recuperação Lenta</h3>
        <ul>
            <li><strong>Problema:</strong> Recuperação pós-crise foi prolongada, especialmente em economias avançadas</li>
            <li><strong>Lição:</strong> Crises financeiras deixam cicatrizes econômicas duradouras</li>
            <li><strong>Medida corretiva:</strong> Intervenção antecipada e decisiva para evitar aprofundamento da crise</li>
        </ul>

        <h3>Desigualdade</h3>
        <ul>
            <li><strong>Problema:</strong> Custos da crise foram desproporcionalmente suportados por grupos vulneráveis</li>
            <li><strong>Lição:</strong> Crises financeiras podem exacerbar desigualdades econômicas</li>
            <li><strong>Medida corretiva:</strong> Políticas que consideram impactos distributivos de crises e resgates</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[4]:  # Desafios Persistentes
        st.markdown("""
        <div class="tab-content">
        <h3>Eficácia Regulatória</h3>
        <ul>
            <li><strong>Desafio:</strong> Evitar tanto a regulação excessiva quanto a desregulamentação imprudente</li>
            <li><strong>Questão crítica:</strong> Como calibrar regulação para proteger estabilidade sem sufocar inovação?</li>
        </ul>

        <h3>Inovação Financeira</h3>
        <ul>
            <li><strong>Desafio:</strong> Novas tecnologias e produtos criam riscos desconhecidos</li>
            <li><strong>Questão crítica:</strong> Como regular inovações como fintech, criptomoedas e finanças descentralizadas?</li>
        </ul>

        <h3>Vulnerabilidades Emergentes</h3>
        <ul>
            <li><strong>Desafio:</strong> Riscos migram para setores menos regulados</li>
            <li><strong>Questão crítica:</strong> Como identificar e mitigar novas fontes de risco sistêmico?</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Citação de conclusão
    st.markdown("""
    <div style="margin: 2rem 0; padding: 2rem; text-align: center; background-color: #F3F4F6; border-radius: 10px;">
        <blockquote style="font-size: 1.1rem; font-style: italic; color: #4B5563;">
            "A história não se repete, mas frequentemente rima."
            <br><span style="font-size: 0.9rem;">— Atribuído a Mark Twain</span>
        </blockquote>
        <p style="margin-top: 1rem;">
        A lição mais importante da crise subprime talvez seja a necessidade constante de vigilância e humildade. 
        Os riscos no sistema financeiro evoluem continuamente, exigindo que reguladores, instituições financeiras 
        e participantes do mercado adaptem suas abordagens. A estabilidade financeira nunca é permanente - é um 
        objetivo em constante movimento que requer atenção perpétua.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Recursos adicionais
    st.markdown('<div class="sub-header">Recursos Adicionais para Estudo</div>', unsafe_allow_html=True)
    
    # Dividir em duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Livros Recomendados
        
        * **"A Crise de 2008 e a Economia da Depressão"** - Paul Krugman
        * **"Too Big to Fail"** - Andrew Ross Sorkin
        * **"The Big Short"** - Michael Lewis
        * **"Lords of Finance"** - Liaquat Ahamed
        * **"This Time Is Different"** - Carmen Reinhart e Kenneth Rogoff
        * **"Crashed: How a Decade of Financial Crises Changed the World"** - Adam Tooze
        """)
    
    with col2:
        st.markdown("""
        ### Documentários e Filmes
        
        * **"Inside Job"** (2010) - Documentário
        * **"The Big Short"** (2015) - Filme
        * **"Margin Call"** (2011) - Filme
        * **"Too Big to Fail"** (2011) - Filme para TV
        * **"Frontline: Money, Power and Wall Street"** - Série documental
        * **"Explained: The 2008 Financial Crisis"** - Netflix
        """)
    
# Rodapé
st.markdown("""
<div class="footer">
Desenvolvido como material didático para aulas sobre crises financeiras.<br>
© 2025 - Prof. José Américo – Coppead
</div>
""", unsafe_allow_html=True)

# Adicionar CSS para melhorar a aparência do aplicativo
def add_footer_css():
    st.markdown("""
    <style>
        .viewerBadge {
            display: none !important;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

add_footer_css()

