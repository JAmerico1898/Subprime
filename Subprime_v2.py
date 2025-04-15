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


# Page configuration
st.set_page_config(
    page_title="Subprime Crisis: Timeline and Impacts",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to apply custom CSS
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

# Main title
st.markdown('<div class="main-header">Subprime Crisis: Timeline and Global Impacts</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
This interactive application presents a detailed analysis of the 2008 Subprime Crisis, 
including its timeline, causes, global impacts, and lessons learned. 
Navigate through different sections using the sidebar menu.
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a section:",
    ["Introduction", 
     "Timeline", 
     "Housing Bubble", 
     "Global Impact",
     "Securitization",
     "Regulatory Responses",
     "Lessons Learned"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**About the application**

This application was developed as educational material for financial crisis classes.

© 2025 - Prof. José Américo – Coppead
""")

# Introduction page content
if page == "Introduction":
    st.markdown('<div class="sub-header">Overview of the Subprime Crisis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        The 2008 subprime crisis was the most severe financial crisis since the Great Depression, 
        causing profound impacts on the global economy and fundamentally changing the international 
        financial system.
        
        ### What was the subprime crisis?
        
        The crisis originated in the US housing market, centered on high-risk (subprime) mortgage loans 
        granted to borrowers with questionable credit history. The securitization of these loans into 
        complex financial instruments spread risk throughout the global financial system.
        
        ### Why study this crisis?
        
        * Reveals vulnerabilities in the modern financial system
        * Demonstrates how problems in one sector can propagate globally
        * Led to fundamental changes in financial regulation
        * Offers valuable lessons to prevent future crises
        
        Explore the different sections of this application to understand the timeline, causes, 
        impacts, and consequences of this historic crisis.
        """)
    
    with col2:
        st.markdown("""
        ### Key Facts
        
        * **Estimated loss:** More than $2 trillion globally
        
        * **Market decline:** Major stock indices fell more than 50%
        
        * **Government bailouts:** Hundreds of billions of dollars in interventions
        
        * **US unemployment:** Increased from 5% to more than 10%
        
        * **Global recession:** First contraction of global GDP since 1945
        
        * **Failed institutions:** Lehman Brothers, Washington Mutual, Bear Stearns and others
        """)
        
        st.markdown('<div class="info-box"><strong>Start exploring!</strong><br>Use the navigation menu to access different sections of the application.</div>', unsafe_allow_html=True)

# Timeline page content
elif page == "Timeline":
    st.markdown('<div class="sub-header">Crisis Timeline</div>', unsafe_allow_html=True)
    
    # Create period options for the timeline
    timeline_periods = [
        "Background (2001-2006)", 
        "Early Warning Signs (2006-2007)", 
        "Crisis Outbreak (2007-2008)",
        "Peak of the Crisis (2008)", 
        "Global Developments (2008-2010)",
        "Policy Responses (2008-2010)",
        "Consequences (2010-2015)",
        "Legacy and Transformations (2015-2023)"
    ]
    
    selected_period = st.selectbox("Select a period from the timeline:", timeline_periods)
    
    # Timeline data for each period
    timeline_data = {
        "Background (2001-2006)": [
            {"date": "2001", "description": "After the dot-com bubble burst, the Federal Reserve reduced interest rates to just 1% to stimulate the economy."},
            {"date": "2001-2003", "description": "Beginning of financial deregulation. The banking sector began to aggressively expand mortgage credit."},
            {"date": "2003-2006", "description": "Proliferation of subprime (high-risk) loans and complex financial instruments such as CDOs (Collateralized Debt Obligations) and MBS (Mortgage-Backed Securities)."},
            {"date": "2001-2006", "description": "Housing prices in the US rose by an average of 85%, creating a speculative bubble in the real estate market."}
        ],
        "Early Warning Signs (2006-2007)": [
            {"date": "Mid-2006", "description": "Housing prices peaked and began to fall. Default rates on subprime loans began to rise."},
            {"date": "Feb 2007", "description": "HSBC bank announced losses of $10.5 billion related to the subprime market."},
            {"date": "Apr 2007", "description": "New Century Financial, one of the largest subprime lenders in the US, filed for bankruptcy."},
            {"date": "Jun-Jul 2007", "description": "Rating agencies (Moody's, S&P) downgraded hundreds of securities backed by subprime mortgages."},
            {"date": "Aug 2007", "description": "BNP Paribas suspended three funds due to the impossibility of valuing subprime assets. This event is often considered the formal beginning of the crisis."}
        ],
        "Crisis Outbreak (2007-2008)": [
            {"date": "Sep 2007", "description": "Northern Rock, a British bank, experienced a bank run and needed a rescue from the Bank of England."},
            {"date": "Oct 2007", "description": "UBS and Citigroup announced billion-dollar losses related to the subprime market."},
            {"date": "Dec 2007", "description": "Federal Reserve created the Term Auction Facility (TAF) to provide liquidity to the banking system."},
            {"date": "Jan-Feb 2008", "description": "Major global banks announced massive losses. The Fed aggressively cut interest rates."},
            {"date": "Mar 2008", "description": "Bear Stearns, the fifth-largest US investment bank, was sold to JPMorgan Chase with help from the Federal Reserve for just $10 per share, well below its previous market value."}
        ],
        "Peak of the Crisis (2008)": [
            {"date": "Sep 2008 (7th)", "description": "The US government took control of Fannie Mae and Freddie Mac, mortgage market giants."},
            {"date": "Sep 2008 (15th)", "description": "Lehman Brothers, the fourth-largest US investment bank, declared bankruptcy. This is considered the most dramatic moment of the crisis."},
            {"date": "Sep 2008 (16th)", "description": "Insurance company AIG received an $85 billion bailout from the US government."},
            {"date": "Sep 2008 (16-20th)", "description": "Panic in global markets. Freezing of interbank credit. Bank runs at various institutions."},
            {"date": "Oct 2008", "description": "US Congress approved the TARP (Troubled Asset Relief Program) of $700 billion to buy toxic assets and recapitalize banks."},
            {"date": "Nov-Dec 2008", "description": "The US officially entered a recession. The unemployment rate soared. Bailouts for American automakers."}
        ],
        "Global Developments (2008-2010)": [
            {"date": "Oct 2008", "description": "Iceland: collapse of the country's three largest banks, leading to the virtual bankruptcy of the nation."},
            {"date": "Oct-Nov 2008", "description": "Central banks around the world coordinated interest rate cuts. IMF rescued countries like Hungary, Ukraine, and Pakistan."},
            {"date": "Dec 2008", "description": "China announced a $586 billion stimulus package. Japan, UK, and European Union launched their own packages."},
            {"date": "Jan-Feb 2009", "description": "Global economy entered a synchronized recession. Global GDP contracted by 0.6% in 2009, the first contraction since World War II."},
            {"date": "Feb 2009", "description": "US approved the American Recovery and Reinvestment Act of $787 billion."},
            {"date": "2009-2010", "description": "Beginning of the European sovereign debt crisis, especially in Greece, Ireland, Portugal, Spain, and Italy."}
        ],
        "Policy Responses (2008-2010)": [
            {"date": "Oct 2008", "description": "G7 committed to taking 'all necessary measures' to stabilize the financial system."},
            {"date": "Nov 2008", "description": "First G20 summit focused on the financial crisis, marking the rise of this group as the main global economic forum."},
            {"date": "Mar 2009", "description": "Federal Reserve initiated the first Quantitative Easing (QE) program, buying $1.25 trillion in mortgage-backed securities."},
            {"date": "Apr 2009", "description": "G20 committed to providing $1.1 trillion in resources to combat the global crisis."},
            {"date": "Jul 2010", "description": "Dodd-Frank Act approved in the US, the biggest financial reform since the Great Depression."},
            {"date": "Sep 2010", "description": "Basel III agreement established new rules for bank capital and liquidity at the global level."}
        ],
        "Consequences (2010-2015)": [
            {"date": "2010-2012", "description": "Slowdown in global economic recovery. Persistence of high unemployment in many developed countries."},
            {"date": "2010-2014", "description": "European debt crisis intensified, forcing bailouts of Greece, Ireland, Portugal, and intervention in the Spanish banking sector."},
            {"date": "2011-2013", "description": "Social protests such as Occupy Wall Street and anti-austerity demonstrations in Europe reflected popular discontent."},
            {"date": "2012-2014", "description": "Central banks maintained ultra-loose monetary policies. ECB promised to do 'whatever it takes' to save the euro."},
            {"date": "2013-2015", "description": "Uneven recovery: US recovered more quickly, while Europe and Japan faced prolonged stagnation. Emerging economies slowed down."}
        ],
        "Legacy and Transformations (2015-2023)": [
            {"date": "2015-2018", "description": "Federal Reserve began gradual monetary normalization. Moderate but stable global growth, with increasing inequalities."},
            {"date": "2016-2018", "description": "Rise of populist and nationalist political movements in various countries, partially attributed to the socioeconomic consequences of the crisis."},
            {"date": "2018-2019", "description": "Revisions and relaxation of some banking regulations implemented post-crisis, especially in the US."},
            {"date": "2020-2021", "description": "During the COVID-19 crisis, lessons from the 2008 crisis allowed faster and more coordinated responses from central banks and governments."},
            {"date": "2022-2023", "description": "Return of inflation and rising interest rates after years of expansionary monetary policy, testing the resilience of the reformed financial system."}
        ]
    }
    
    # Colors for different periods
    period_colors = {
        "Background (2001-2006)": "#FF9E80",
        "Early Warning Signs (2006-2007)": "#FFCC80",
        "Crisis Outbreak (2007-2008)": "#FFD180",
        "Peak of the Crisis (2008)": "#F57C00",
        "Global Developments (2008-2010)": "#EF6C00",
        "Policy Responses (2008-2010)": "#BF360C",
        "Consequences (2010-2015)": "#B71C1C",
        "Legacy and Transformations (2015-2023)": "#880E4F"
    }
    
    # Display events for the selected period
    st.markdown(f'<div style="background-color: {period_colors[selected_period]}22; padding: 1rem; border-radius: 5px; border-left: 5px solid {period_colors[selected_period]}; margin-bottom: 1rem;"><h3 style="margin:0; color: #333;">{selected_period}</h3></div>', unsafe_allow_html=True)
    
    for event in timeline_data[selected_period]:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-date">{event['date']}</div>
            <div class="timeline-description">{event['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Simplified visual timeline
    st.markdown('<div class="chart-title">Timeline Overview</div>', unsafe_allow_html=True)
    

    # Create timeline table with color formatting
    timeline_data = {
        "Period": ["2001-2006", "2006-2007", "2007-2008", "2008 (Sep)", "2008-2010", "2008-2010", "2010-2015", "2015-2023"],
        "Phase": ["Bubble Formation", "Warning", "Initial Crisis", "Collapse", "Global Contagion", "Intervention", "Recovery", "Transformation"],
        "Key Events": [
            "Low interest rates, deregulation, subprime credit expansion",
            "Falling housing prices, increasing defaults, first bankruptcies",
            "Northern Rock, major bank losses, Bear Stearns sale",
            "Lehman Brothers collapses, market panic, AIG bailout, TARP approved",
            "Iceland crisis, global stimulus packages, synchronized recession",
            "G20 coordination, QE programs, regulatory reforms",
            "European debt crisis, slow recovery, prolonged low interest rates",
            "Monetary normalization, revision of some regulations, lessons for the COVID-19 crisis"
        ]
    }

    # Colors for each phase
    colors = [
        "#FF9E80", "#FFCC80", "#FFD180", "#F57C00", 
        "#EF6C00", "#BF360C", "#B71C1C", "#880E4F"
    ]

    # Create DataFrame
    df_timeline = pd.DataFrame(timeline_data)

    # Generate HTML for colored table
    html_table = '<table style="width:100%; border-collapse: collapse; margin-bottom: 30px;">'
    html_table += '<tr><th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Period</th>'
    html_table += '<th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Phase</th>'
    html_table += '<th style="padding: 10px; text-align: left; border-bottom: 2px solid #ddd;">Key Events</th></tr>'

    for i in range(len(df_timeline)):
        bg_color = f"{colors[i]}33"  # Add transparency to color
        border_color = colors[i]
        html_table += f'<tr style="background-color: {bg_color}; border-left: 5px solid {border_color};">'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd;">{df_timeline["Period"][i]}</td>'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd; font-weight: bold;">{df_timeline["Phase"][i]}</td>'
        html_table += f'<td style="padding: 12px; border-bottom: 1px solid #ddd;">{df_timeline["Key Events"][i]}</td>'
        html_table += '</tr>'

    html_table += '</table>'

    # Display table in Streamlit
    st.markdown(html_table, unsafe_allow_html=True)

    # Add key events in list format
    st.markdown('<div class="chart-title">Crucial Events</div>', unsafe_allow_html=True)

    events = [
        {"date": "August 2007", "event": "BNP Paribas suspends funds - Formal beginning of the crisis"},
        {"date": "March 2008", "event": "Emergency sale of Bear Stearns to JPMorgan Chase"},
        {"date": "September 2008", "event": "Lehman Brothers bankruptcy - Most dramatic moment of the crisis"},
        {"date": "October 2008", "event": "Approval of TARP ($700 billion) to stabilize the financial system"},
        {"date": "March 2009", "event": "Beginning of the first Quantitative Easing (QE) program by the Federal Reserve"},
        {"date": "July 2010", "event": "Approval of the Dodd-Frank Act - Biggest financial reform since the Great Depression"}
    ]

    for event in events:
        st.markdown(f"""
        <div style="margin-bottom: 10px; padding: 10px; background-color: #f8f9fa; border-left: 3px solid #d63031; border-radius: 3px;">
            <span style="font-weight: bold; color: #d63031;">{event['date']}</span>: {event['event']}
        </div>
        """, unsafe_allow_html=True)
        
    
    def create_bokeh_timeline():
        # Configure data
        phases = ["Bubble Formation", "Warning", "Initial Crisis", "Collapse", 
                "Global Contagion", "Intervention", "Recovery", "Transformation"]
        
        start_years = [2001, 2006, 2007, 2008, 2008.75, 2008.75, 2010, 2015]
        end_years = [2006, 2007, 2008, 2008.75, 2010, 2010.5, 2015, 2023]
        
        # Important events
        event_x = [2006.5, 2008.7, 2010, 2010.5]
        event_y = ["Warning", "Collapse", "Intervention", "Recovery"]
        event_text = ["Beginning of housing decline", "Lehman Brothers bankruptcy", 
                    "Dodd-Frank & Basel III", "European debt crisis"]
        
        # Data for the chart
        source = ColumnDataSource(data=dict(
            phase=phases,
            start=start_years,
            end=end_years,
            duration=[e-s for s, e in zip(start_years, end_years)],
            color=Spectral8[::-1]  # Invert palette for similar colors
        ))
        
        # Data for events
        event_source = ColumnDataSource(data=dict(
            x=event_x,
            y=event_y,
            text=event_text
        ))
        
        # Create figure
        p = figure(
            y_range=phases,
            x_range=(2000, 2024),
            height=500,
            title="Subprime Crisis Timeline",
            toolbar_location=None,
            sizing_mode="stretch_width"
        )
        
        # Add horizontal bars
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
        
        # Add labels inside bars
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
        
        # Add circles for events
        p.circle(
            x='x',
            y='y',
            size=10,
            source=event_source,
            color='black',
            alpha=0.8
        )
        
        # Add labels for events
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
        
        # Style the chart
        p.xaxis.axis_label = "Year"
        p.yaxis.axis_label = ""
        p.outline_line_color = None
        p.grid.grid_line_color = None
        
        # Configure year ticks
        p.xaxis.ticker = list(range(2001, 2024, 2))
        
        # Return HTML
        return file_html(p, CDN)

    # Within the timeline section, replace the chart code with the following:
    html = create_bokeh_timeline()
    components.html(html, height=550)

    # Don't forget to add bokeh to dependencies
            
    
# Housing Bubble page content
elif page == "Housing Bubble":
    st.markdown('<div class="sub-header">Evolution of the US Housing Bubble</div>', unsafe_allow_html=True)
    
    # Case-Shiller S&P/Case-Shiller 20-City Composite Home Price Index data
    dates = [2000, 2000.5, 2001, 2001.5, 2002, 2002.5, 2003, 2003.5, 2004, 2004.5, 2005, 2005.5, 2006, 2006.5, 2007, 2007.5, 2008, 2008.5, 2008.75, 2009, 2009.5, 2010, 2010.5, 2011, 2011.5, 2012, 2012.5]
    values = [100.0, 105.2, 110.8, 116.5, 121.9, 129.6, 138.1, 146.7, 157.6, 170.9, 181.5, 198.6, 204.8, 206.2, 198.4, 189.2, 173.5, 162.8, 158.1, 147.8, 143.2, 145.6, 147.8, 141.9, 142.2, 140.6, 145.3]
    
    # Create DataFrame
    df_housing = pd.DataFrame({
        'Date': dates,
        'Index': values
    })
    
    # Add column for phases
    conditions = [
        (df_housing['Date'] <= 2006.5),
        (df_housing['Date'] > 2006.5) & (df_housing['Date'] <= 2008.75),
        (df_housing['Date'] > 2008.75)
    ]
    phases = ['Bubble Formation', 'Bubble Burst', 'Crisis and Slow Recovery']
    colors = ['rgba(255, 200, 0, 0.2)', 'rgba(255, 100, 0, 0.2)', 'rgba(255, 0, 0, 0.2)']
    
    df_housing['Phase'] = np.select(conditions, phases)
    
    # Important events
    events = [
        {'date': 2006.5, 'event': 'Bubble peak', 'value': 206.2},
        {'date': 2007.5, 'event': 'Subprime crisis begins', 'value': 189.2},
        {'date': 2008.75, 'event': 'Lehman Brothers collapse', 'value': 158.1}
    ]
    
    # Create chart with Plotly
    fig = px.line(df_housing, x='Date', y='Index', title='')
    
    # Add shaded areas for phases
    for phase, color in zip(phases, colors):
        phase_data = df_housing[df_housing['Phase'] == phase]
        if not phase_data.empty:
            x_range = [phase_data['Date'].min(), phase_data['Date'].max()]
            y_range = [df_housing['Index'].min() * 0.95, df_housing['Index'].max() * 1.05]
            
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
    
    # Add vertical lines and annotations for important events
    for event in events:
        fig.add_vline(x=event['date'], line_dash="dash", line_color="red", line_width=1)
        fig.add_annotation(
            x=event['date'],
            y=event['value'],
            text=event['event'],
            showarrow=True,
            arrowhead=1,
            ax=0,
            ay=-40
        )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Case-Shiller Index (2000=100)",
        height=600,
        hovermode="x unified",
        legend_title="Phase",
        xaxis=dict(
            tickmode='array',
            tickvals=[2000, 2002, 2004, 2006, 2007, 2008, 2009, 2010, 2012],
            ticktext=['2000', '2002', '2004', '2006', '2007', '2008', '2009', '2010', '2012']
        ),
        shapes=[
            # Horizontal line for 2000 level
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
    
    fig.update_traces(line=dict(color='#FF5722', width=3), hovertemplate='Year: %{x}<br>Index: %{y:.1f}')
    
    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    # Add explanation
    st.markdown("""
    <div class="info-box">
    <h3>Anatomy of the Housing Bubble</h3>
    <p>The chart above shows the evolution of the Case-Shiller Index, which measures residential home prices in 20 major metropolitan areas in the US. Note the three distinct phases:</p>
    <ol>
        <li><strong>Bubble Formation (2000-2006):</strong> Prices rose more than 100% in just 6 years, driven by low interest rates, loose regulation, and financial innovations that expanded mortgage credit.</li>
        <li><strong>Bubble Burst (2006-2008):</strong> When interest rates rose and default rates increased, prices began to fall, creating a vicious cycle of foreclosures and further price drops.</li>
        <li><strong>Crisis and Slow Recovery (2008-2012):</strong> After the collapse of Lehman Brothers, the crisis deepened and prices continued to fall, with a very slow recovery that only began in 2012.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Add factors that contributed to the housing bubble
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-title">Factors that Contributed to the Bubble</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Loose monetary policy**: Low interest rates after the dot-com crisis
        - **Government policy**: Incentives to expand home ownership
        - **Financial innovation**: Securitization and complex structured products
        - **Inadequate regulation**: Weak supervision of the mortgage market
        - **Distorted incentives**: Mortgage originators with no responsibility for risk
        - **Optimistic valuations**: Expectation of continuous property appreciation
        - **Failed risk ratings**: Rating agencies assigning AAA to toxic products
        """)
    
    with col2:
        st.markdown('<div class="chart-title">Subprime Mortgage Rates (2000-2008)</div>', unsafe_allow_html=True)
        
        # Fictional data to illustrate the growth of subprime mortgages
        subprime_years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
        subprime_share = [8, 9, 12, 14, 18, 22, 23.5, 21, 15]
        
        # Create bar chart
        fig_subprime = px.bar(
            x=subprime_years, 
            y=subprime_share,
            labels={'x': 'Year', 'y': '% of Mortgage Market'},
            title=''
        )
        
        fig_subprime.update_traces(marker_color=['#90CAF9', '#90CAF9', '#90CAF9', '#90CAF9', '#FFAB91', '#FF8A65', '#FF7043', '#F4511E', '#D84315'])
        
        fig_subprime.update_layout(
            height=300,
            xaxis_title="Year",
            yaxis_title="% of Mortgage Market",
            hovermode="x"
        )
        
        st.plotly_chart(fig_subprime, use_container_width=True)
        
        st.markdown("""
        <div style="font-size: 0.8rem; color: #666; text-align: center; margin-top: -15px;">
        Share of subprime loans in the US mortgage market.
        </div>
        """, unsafe_allow_html=True)

# Global Impact page content
elif page == "Global Impact":
    st.markdown('<div class="sub-header">Global Economic Impacts of the Crisis</div>', unsafe_allow_html=True)
    
    # Offers options for different impact visualizations
    impact_metric = st.radio(
        "Select an impact metric:",
        ["GDP Growth", "Unemployment", "Public Debt"],
        horizontal=True
    )
    
    if impact_metric == "GDP Growth":
        # GDP growth data (annual % change)
        gdp_data = {
            'Country': ['USA', 'UK', 'Japan', 'Germany', 'France', 'Brazil', 'China', 'India', 'Russia'],
            '2007': [1.9, 2.7, 1.7, 3.0, 2.4, 6.1, 14.2, 9.8, 8.5],
            '2008': [-0.1, -0.3, -1.1, 0.8, 0.3, 5.1, 9.7, 3.9, 5.2],
            '2009': [-2.5, -4.2, -5.4, -5.7, -2.9, -0.1, 9.4, 8.5, -7.8]
        }
        
        df_gdp = pd.DataFrame(gdp_data)
        
        # Reorganize data to "long" format for Plotly
        df_gdp_long = pd.melt(df_gdp, id_vars=['Country'], var_name='Year', value_name='GDP Growth (%)')
        
        # Create bar chart
        fig = px.bar(
            df_gdp_long, 
            x='Country', 
            y='GDP Growth (%)', 
            color='Year',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2008': '#FFC107', '2009': '#FF5722'},
            title='Impact on Economic Growth between 2007-2009',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="GDP Growth (%)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impact on Economic Growth</h3>
        <p>The crisis caused a severe global economic contraction:</p>
        <ul>
            <li><strong>Advanced economies:</strong> Were the hardest hit, with severe contractions in 2009.</li>
            <li><strong>Russia:</strong> Among emerging economies, suffered the largest contraction due to commodity dependence.</li>
            <li><strong>China and India:</strong> Maintained positive growth, although slowed, partly due to large stimulus packages.</li>
            <li><strong>Brazil:</strong> Experienced a brief contraction followed by rapid recovery in 2010.</li>
        </ul>
        <p>This was the first synchronized global recession since World War II.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif impact_metric == "Unemployment":
        # Unemployment data (% of labor force)
        unemployment_data = {
            'Country': ['USA', 'UK', 'Japan', 'Germany', 'France', 'Spain', 'Greece'],
            '2007': [4.6, 5.3, 3.9, 8.6, 8.0, 8.2, 8.4],
            '2008': [5.8, 5.6, 4.0, 7.5, 7.4, 11.3, 7.8],
            '2009': [9.3, 7.6, 5.1, 7.8, 9.1, 17.9, 9.6],
            '2010': [9.6, 7.8, 5.1, 7.1, 9.3, 19.9, 12.7]
        }
        
        df_unemployment = pd.DataFrame(unemployment_data)
        
        # Reorganize data to "long" format for Plotly
        df_unemp_long = pd.melt(df_unemployment, id_vars=['Country'], var_name='Year', value_name='Unemployment Rate (%)')
        
        # Create bar chart
        fig = px.bar(
            df_unemp_long, 
            x='Country', 
            y='Unemployment Rate (%)', 
            color='Year',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2008': '#FFC107', '2009': '#FF5722', '2010': '#9C27B0'},
            title='Evolution of Unemployment Rate between 2007-2010',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="Unemployment Rate (%)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impact on Labor Market</h3>
        <p>The crisis caused a significant increase in unemployment in many countries:</p>
        <ul>
            <li><strong>USA:</strong> The unemployment rate doubled, rising from 4.6% to over 9%.</li>
            <li><strong>Southern Europe:</strong> Spain and Greece suffered the most severe impacts, with unemployment rates reaching nearly 20% in Spain.</li>
            <li><strong>Germany:</strong> Experienced less impact due to flexible labor policies (Kurzarbeit) that allowed for hour reductions instead of layoffs.</li>
            <li><strong>Slow recovery:</strong> In most countries, unemployment continued to rise even after GDP began to recover (phenomenon known as "jobless recovery").</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Public Debt
        # Public debt data (% of GDP)
        debt_data = {
            'Country': ['USA', 'UK', 'Japan', 'Germany', 'France', 'Italy', 'Greece', 'Spain', 'Ireland'],
            '2007': [64.0, 43.5, 183.0, 63.7, 64.2, 103.1, 107.4, 36.3, 24.8],
            '2010': [91.4, 75.6, 215.8, 82.5, 82.3, 119.1, 146.2, 60.1, 86.8],
            'Increase': [27.4, 32.1, 32.8, 18.8, 18.1, 16.0, 38.8, 23.8, 62.0]
        }
        
        df_debt = pd.DataFrame(debt_data)
        
        # Reorganize data to "long" format for Plotly
        df_debt_long = pd.melt(df_debt, id_vars=['Country'], var_name='Period', value_name='Debt (% of GDP)')
        
        # Create bar chart
        fig = px.bar(
            df_debt_long, 
            x='Country', 
            y='Debt (% of GDP)', 
            color='Period',
            barmode='group',
            color_discrete_map={'2007': '#4CAF50', '2010': '#FF5722', 'Increase': '#F44336'},
            title='Public Debt Increase between 2007-2010 due to Bailouts and Economic Stimulus',
            height=600
        )
        
        fig.update_layout(xaxis_title="", yaxis_title="Public Debt (% of GDP)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="info-box">
        <h3>Impact on Public Finances</h3>
        <p>The crisis led to a dramatic increase in public debts due to:</p>
        <ul>
            <li><strong>Bank bailouts:</strong> Governments injected hundreds of billions to save financial institutions.</li>
            <li><strong>Fiscal stimulus packages:</strong> Public spending to offset the fall in private demand.</li>
            <li><strong>Reduced tax revenues:</strong> Due to economic contraction and rising unemployment.</li>
            <li><strong>Ireland:</strong> Recorded the largest relative increase, with its debt more than tripling in three years.</li>
            <li><strong>Greece:</strong> The high pre-crisis debt combined with the increase led to the European sovereign debt crisis.</li>
        </ul>
        <p>This increase in public debt subsequently led to austerity policies in many countries, especially in Europe.</p>
        </div>
        """, unsafe_allow_html=True)

# Securitization page content
elif page == "Securitization":
    st.markdown('<div class="sub-header">Financial Innovations and Securitization</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    Securitization and complex financial innovations were central elements in the subprime crisis. 
    This diagram illustrates how high-risk mortgage loans were transformed into complex financial 
    products and distributed throughout the global financial system.
    </div>
    """, unsafe_allow_html=True)
    
    # Create securitization diagram with networkx and matplotlib
    st.markdown('<div class="chart-title">Securitization Process Flow</div>', unsafe_allow_html=True)
    
    # Create a simplified diagram of the securitization process
    G = nx.DiGraph()
    
    # Add nodes for different participants and instruments
    nodes = {
        "Households": {"type": "participant", "level": 0, "pos": (0, 4.6)},
        "Originating Banks": {"type": "bank", "level": 1, "pos": (1.8, 4)},
        "Prime Mortgages": {"type": "asset", "level": 1.5, "pos": (4, 5)},
        "Subprime Mortgages": {"type": "asset", "level": 1.5, "pos": (4, 3)},
        "Investment Banks": {"type": "bank", "level": 2, "pos": (6, 4)},
        "SPV": {"type": "special", "level": 3, "pos": (8, 4.7)},
        "SIV": {"type": "special", "level": 3, "pos": (8, 3.3)},
        "MBS": {"type": "asset", "level": 4, "pos": (10, 4)},
        "CDO": {"type": "asset", "level": 5, "pos": (12, 4)},
        "AAA Tranche": {"type": "asset", "level": 6, "pos": (13, 5)},
        "BBB Tranche": {"type": "asset", "level": 6, "pos": (13.15, 3.25)},
        "European Bks": {"type": "bank", "level": 6.3, "pos": (14.5, 4)},
        "Pension Funds": {"type": "investor", "level": 7, "pos": (17, 5)},
        "Hedge Funds": {"type": "investor", "level": 7, "pos": (16.85, 3.25)},
        "CDS": {"type": "risk", "level": 5.5, "pos": (12, 2)},
        "Global System": {"type": "investor", "level": 8, "pos": (18, 4)},
    }
    
    # Add nodes to the graph
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)
    
    # Add edges
    edges = [
        ("Households", "Originating Banks", "Take loans"),
        ("Originating Banks", "Prime Mortgages", "Originate"),
        ("Originating Banks", "Subprime Mortgages", "Originate"),
        ("Originating Banks", "Investment Banks", "Sell mortgages"),
        ("Prime Mortgages", "Investment Banks", ""),
        ("Subprime Mortgages", "Investment Banks", ""),
        ("Investment Banks", "SPV", "Create"),
        ("Investment Banks", "SIV", "Kept off-balance"),
        ("SPV", "MBS", "Issue"),
        ("MBS", "CDO", "Structure"),
        ("CDO", "AAA Tranche", "Segment by risk"),
        ("CDO", "European Bks", "Buy"),
        ("CDO", "BBB Tranche", "Segment by risk"),
        ("CDO", "CDS", "Protection against default"),
        ("AAA Tranche", "Pension Funds", "Buy"),
        ("BBB Tranche", "Hedge Funds", "Buy"),
        ("European Bks", "Global System", "Risk propagation"),
        ("Pension Funds", "Global System", "Risk propagation"),
        ("Hedge Funds", "Global System", "Risk propagation"),
        ("CDS", "Global System", "Interconnection")
    ]
    
    for u, v, label in edges:
        G.add_edge(u, v, label=label)
    
    # Create plot
    plt.figure(figsize=(14, 8))
    pos = nx.get_node_attributes(G, 'pos')
    
    # Define colors based on node type
    color_map = []
    for node in G:
        node_type = G.nodes[node]['type']
        if node_type == 'participant':
            color_map.append('#E1BEE7')  # Light lilac
        elif node_type == 'bank':
            color_map.append('#BBDEFB')  # Light blue
        elif node_type == 'asset':
            color_map.append('#FFF9C4')  # Light yellow
        elif node_type == 'investor':
            color_map.append('#C8E6C9')  # Light green
        elif node_type == 'risk':
            color_map.append('#FFCDD2')  # Light red
        elif node_type == 'special':
            color_map.append('#D1C4E9')  # Light purple
    
    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=color_map, alpha=0.8, edgecolors='gray', linewidths=1)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=15, arrowstyle='->')
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
    
    # Add labels to edges
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
    
    # Add legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#E1BEE7', markersize=10, label='Participants'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#BBDEFB', markersize=10, label='Banks'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFF9C4', markersize=10, label='Assets'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#C8E6C9', markersize=10, label='Investors'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFCDD2', markersize=10, label='Risk Instruments'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#D1C4E9', markersize=10, label='Special Vehicles')
    ]
    
    plt.legend(handles=legend_elements, loc='lower right')
    plt.axis('off')
    plt.tight_layout()
    
    # Display the chart in Streamlit
    st.pyplot(plt)
    
    # Explanations about financial instruments
    st.markdown('<div class="sub-header">Complex Financial Instruments</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### MBS (Mortgage-Backed Securities)
        Securities backed by mortgages, which group hundreds or thousands of mortgage loans into a single financial product. Investors who buy MBS receive payments based on the cash flow from the underlying loans.
        
        ### CDO (Collateralized Debt Obligations)
        Structured products that group various cash flow-generating assets (including MBS) and divide them into "tranches" with different levels of risk and return. Upper tranches (AAA) had priority in receiving cash flows, while lower ones absorbed the first losses.
        
        ### CDO² (CDO of CDOs)
        An additional layer of complexity: CDOs composed of tranches of other CDOs. This re-securitization made it extremely difficult to assess the real risks of the underlying assets.
        """)
    
    with col2:
        st.markdown("""
        ### CDS (Credit Default Swaps)
        Insurance contracts that protected against default risk. The buyer paid a periodic premium to the seller, who guaranteed compensation in case of a "credit event" (such as default). They were widely used for speculation, not just for risk protection.
        
        ### SIV (Structured Investment Vehicles)
        Entities created by banks to hold assets off-balance sheet. SIVs issued short-term commercial paper to finance the purchase of long-term assets such as MBS, creating a maturity mismatch that proved fatal during the crisis.
        
        ### SPV (Special Purpose Vehicles)
        Legal entities created specifically to isolate financial risks. They were fundamental in the securitization process, allowing banks to transfer assets and their associated risks off their balance sheets.
        """)
    
    st.markdown("""
    <div class="info-box">
    <h3>Fundamental Problems of the Securitization Model</h3>
    <ul>
        <li><strong>Distorted incentives:</strong> The "originate-to-distribute" model removed the incentive for rigorous credit risk assessment.</li>
        <li><strong>Opacity and complexity:</strong> Investors couldn't adequately assess the risks of the structured products they were buying.</li>
        <li><strong>Failures in rating agencies:</strong> Conflicts of interest led to overly optimistic classification of toxic products.</li>
        <li><strong>Hidden risk concentration:</strong> Banks maintained significant exposure through credit lines and implicit guarantees.</li>
        <li><strong>Excessive leverage:</strong> Securitization allowed institutions to circumvent capital requirements and dramatically increase their leverage.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Regulatory Responses page content
elif page == "Regulatory Responses":
    st.markdown('<div class="sub-header">Regulatory Responses to the Crisis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    After the crisis, governments and regulators implemented a series of reforms to correct the flaws 
    revealed by the crisis and strengthen the financial system. The tables below summarize the main 
    measures by region.
    </div>
    """, unsafe_allow_html=True)
    
    # Tables of regulatory responses
    region = st.radio(
        "Select a region:",
        ["United States", "European Union", "International (Basel)"],
        horizontal=True
    )
    
    if region == "United States":
        st.markdown("""
        ## Main Regulatory Measures in the United States
        
        | Measure | Year | Main Objectives | Impacts |
        |--------|-----|----------------------|----------|
        | **Dodd-Frank Act** | 2010 | • Greater supervision of systemically important institutions;  • Creation of the Financial Stability Oversight Council;  • Regulation of OTC derivatives;  • Creation of the Consumer Financial Protection Bureau;  • Volcker Rule (limits proprietary trading) | • Increased capital requirements for banks;  • Greater transparency in the derivatives market;  • Restrictions on speculative activities of banks;  • Enhanced consumer financial protection |
        | **Stress Tests** | 2009-present | • Assess banks' ability to withstand adverse scenarios;  • Identify systemic vulnerabilities | • Strengthening of banking resilience;  • Greater transparency about risks;  • Basis for additional capital requirements |
        | **Liquidity Rules** | 2013-2015 | • Liquidity Coverage Ratio (LCR);  • Net Stable Funding Ratio (NSFR) | • Reduced vulnerability to liquidity shocks;  • Less dependence on short-term funding |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Focus of the US Approach</h3>
        <p>The US regulatory response focused primarily on:</p>
        <ul>
            <li>Greater financial consumer protection</li>
            <li>Enhanced supervision of systemically important institutions</li>
            <li>Greater transparency and regulation of derivatives markets</li>
            <li>Limits on bank risk-taking</li>
        </ul>
        <p>However, since 2018, some parts of the Dodd-Frank Act have been relaxed, especially for mid-sized banks.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif region == "European Union":
        st.markdown("""
        ## Main Regulatory Measures in the European Union
        
        | Measure | Year | Main Objectives | Impacts |
        |--------|-----|----------------------|----------|
        | **Banking Union** | 2012-2014 | • Single Supervisory Mechanism (SSM);  • Single Resolution Mechanism (SRM);  • Deposit Guarantee Scheme | • Centralized supervision of the largest European banks;  • Reduction of the bank-sovereign nexus;  • Harmonized bank resolution process |
        | **CRD IV/CRR** | 2013 | • Implementation of Basel III in Europe;  • More stringent capital requirements;  • Limitation of bank bonuses | • Increase in regulatory capital;  • Introduction of conservation and countercyclical buffers;  • Controls on financial sector remuneration |
        | **MiFID II/MiFIR** | 2018 | • Greater transparency in financial markets;  • Enhanced investor protection;  • Regulation of high-frequency trading | • Stricter rules for order execution;  • Improvement in price formation;  • Reduction of conflicts of interest |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Focus of the European Approach</h3>
        <p>The EU regulatory response focused primarily on:</p>
        <ul>
            <li>Creation of a supranational institutional architecture for banking supervision</li>
            <li>Breaking the vicious circle between banks and sovereign debts</li>
            <li>Harmonization of rules across the single market</li>
            <li>Stricter control over remuneration in the financial sector</li>
        </ul>
        <p>The complete implementation of the Banking Union, however, remains incomplete, with the European Deposit Insurance Scheme still under discussion.</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # International (Basel)
        st.markdown("""
        ## Main International Regulatory Measures (Basel)
        
        | Measure | Year | Main Objectives | Impacts |
        |--------|-----|----------------------|----------|
        | **Basel III** | 2010-2022 | • Increase in the quality and quantity of capital;  • Introduction of countercyclical buffer;  • Limitation of leverage;  • Global liquidity standards | • Tier 1 capital increased from 4% to 6%;  • Introduction of the 3% leverage ratio;  • Enhanced risk management standards;  • More resilient global financial system |
        | **G-SIBs/D-SIBs** | 2011-2012 | • Identification of global and domestic systemically important banks;  • Additional requirements for critical institutions | • Additional capital for systemically important banks;  • Recovery and resolution plans;  • More intense supervision |
        | **FSB** | 2009 | • International coordination of financial regulation;  • Monitoring of systemic risks;  • Implementation of G20 reforms | • Greater global regulatory coordination;  • Peer review of national reforms;  • Global standards for financial institutions |
        """)
        
        st.markdown("""
        <div class="info-box">
        <h3>Focus of the International Approach</h3>
        <p>The international regulatory response focused primarily on:</p>
        <ul>
            <li>Strengthening the resilience of individual banks</li>
            <li>Reducing systemic risk in the global banking system</li>
            <li>Improving cooperation and coordination among national regulators</li>
            <li>Global minimum standards for capital, liquidity, and risk management</li>
        </ul>
        <p>Although Basel III represents a significant strengthening compared to previous agreements, its implementation varies across jurisdictions and deadlines have been extended several times.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Evolution of capital requirements
    st.markdown('<div class="chart-title">Evolution of Bank Capital Requirements (SIB & G-SIB Banks)</div>', unsafe_allow_html=True)
    
    # Data for the capital requirements evolution chart
    basel_years = ["Basel I\n(1988)", "Basel II\n(2004)", "Basel III\n(2010)", "Basel III\n(Final Implementation)"]
    total_capital = [8, 8, 10.5, 13]
    tier1_capital = [4, 4, 6, 8.5]
    core_tier1 = [0, 2, 4.5, 7]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[8, 8, 10.5, 13],
        name='Total Capital',
        marker_color='#90CAF9'
    ))
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[4, 4, 6, 8.5],
        name='Tier 1 Capital',
        marker_color='#42A5F5'
    ))
    
    fig.add_trace(go.Bar(
        x=basel_years,
        y=[0, 2, 4.5, 7],
        name='Core Tier 1 Capital',
        marker_color='#1976D2'
    ))
    
    fig.update_layout(
        barmode='group',
        xaxis=dict(title='Basel Agreement'),
        yaxis=dict(title='% of Risk-Weighted Assets', range=[0, 14]),
        legend=dict(x=0.1, y=1.15, orientation='h'),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div style="font-size: 0.8rem; color: #666; text-align: center; margin-top: -20px;">
    Evolution of minimum capital requirements across Basel agreements. Basel III requirements include the capital conservation buffer.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>Effectiveness of Regulatory Reforms</h3>
    <p>More than a decade after the crisis, debates about the effectiveness of regulatory reforms continue:</p>
    <ul>
        <li><strong>Positive points:</strong> Banking system with more capital and liquidity, greater transparency in derivatives markets, better supervision of systemically important institutions.</li>
        <li><strong>Pending issues:</strong> "Too big to fail" has not been fully resolved, shadow banking continues to grow, regulatory complexity has increased substantially.</li>
        <li><strong>New challenges:</strong> Fintech, cryptocurrencies, and decentralized finance are creating new potential risks outside the traditional regulatory perimeter.</li>
    </ul>
    <p>The COVID-19 crisis in 2020 served as the first major test for the reformed financial system, which demonstrated greater resilience than in 2008, but still with significant support needed from central banks.</p>
    </div>
    """, unsafe_allow_html=True)

# Lessons Learned page content
elif page == "Lessons Learned":
    st.markdown('<div class="sub-header">Lessons from the Subprime Crisis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    The subprime crisis offered valuable lessons about the functioning of financial markets, 
    risk management, financial regulation, and macroeconomic policies. Some of these 
    lessons have been implemented, while others continue to be debated.
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different categories of lessons
    lesson_tabs = st.tabs([
        "Market Failures", 
        "Risk Management", 
        "Governance and Supervision", 
        "Economic Perspectives",
        "Persistent Challenges"
    ])
    
    with lesson_tabs[0]:  # Market Failures
        st.markdown("""
        <div class="tab-content">
        <h3>Asymmetric Information</h3>
        <ul>
            <li><strong>Problem:</strong> Investors relied excessively on rating agencies without understanding complex financial products</li>
            <li><strong>Lesson:</strong> Opacity and complexity in financial products can hide systemic risks</li>
            <li><strong>Corrective measure:</strong> Greater transparency and mandatory risk disclosure</li>
        </ul>

        <h3>Distorted Incentives</h3>
        <ul>
            <li><strong>Problem:</strong> "Originate-to-distribute" model removed incentive for proper risk assessment</li>
            <li><strong>Lesson:</strong> Compensation and incentive structures should be aligned with long-term stability</li>
            <li><strong>Corrective measure:</strong> Risk retention requirements ("skin in the game") for originators</li>
        </ul>

        <h3>Inadequate Regulation</h3>
        <ul>
            <li><strong>Problem:</strong> Shadow banking system operated with limited supervision</li>
            <li><strong>Lesson:</strong> Regulatory arbitrage creates systemic vulnerabilities</li>
            <li><strong>Corrective measure:</strong> Comprehensive supervision based on activities, not just entities</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[1]:  # Risk Management
        st.markdown("""
        <div class="tab-content">
        <h3>Tail Risk</h3>
        <ul>
            <li><strong>Problem:</strong> Models underestimated extreme events and correlations in times of crisis</li>
            <li><strong>Lesson:</strong> "Black swans" occur more frequently than models suggest</li>
            <li><strong>Corrective measure:</strong> More rigorous stress tests and consideration of extreme scenarios</li>
        </ul>

        <h3>Dynamic Correlations</h3>
        <ul>
            <li><strong>Problem:</strong> Diversification failed when correlations between assets increased during the crisis</li>
            <li><strong>Lesson:</strong> Benefits of diversification can disappear when most needed</li>
            <li><strong>Corrective measure:</strong> Risk models should consider dynamic correlations and not just historical data</li>
        </ul>

        <h3>Liquidity Risk</h3>
        <ul>
            <li><strong>Problem:</strong> Institutions relied excessively on short-term funding</li>
            <li><strong>Lesson:</strong> Maturity mismatch can quickly become fatal in periods of stress</li>
            <li><strong>Corrective measure:</strong> Liquidity standards (LCR and NSFR) and enhanced liquidity management</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[2]:  # Governance and Supervision
        st.markdown("""
        <div class="tab-content">
        <h3>Systemic View</h3>
        <ul>
            <li><strong>Problem:</strong> Regulators focused on individual institutions, not the system as a whole</li>
            <li><strong>Lesson:</strong> Stability of individual institutions does not guarantee systemic stability</li>
            <li><strong>Corrective measure:</strong> Creation of macroprudential supervision bodies (e.g., FSOC in the US)</li>
        </ul>

        <h3>Too Big To Fail</h3>
        <ul>
            <li><strong>Problem:</strong> Institutions too big to fail created moral hazard</li>
            <li><strong>Lesson:</strong> The cost of public bailouts is unacceptably high</li>
            <li><strong>Corrective measure:</strong> Additional requirements for systemic banks and resolution regimes</li>
        </ul>

        <h3>International Coordination</h3>
        <ul>
            <li><strong>Problem:</strong> Fragmented response to the global crisis</li>
            <li><strong>Lesson:</strong> Financial markets are global, requiring international regulatory coordination</li>
            <li><strong>Corrective measure:</strong> Strengthening of the FSB and global implementation of Basel standards</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[3]:  # Economic Perspectives
        st.markdown("""
        <div class="tab-content">
        <h3>Asset Bubbles</h3>
        <ul>
            <li><strong>Problem:</strong> Loose monetary policies contributed to the housing bubble</li>
            <li><strong>Lesson:</strong> Monetary policy should consider financial stability, not just inflation</li>
            <li><strong>Corrective measure:</strong> Macroprudential tools to contain unsustainable credit growth</li>
        </ul>

        <h3>Slow Recovery</h3>
        <ul>
            <li><strong>Problem:</strong> Post-crisis recovery was prolonged, especially in advanced economies</li>
            <li><strong>Lesson:</strong> Financial crises leave lasting economic scars</li>
            <li><strong>Corrective measure:</strong> Early and decisive intervention to prevent deepening of the crisis</li>
        </ul>

        <h3>Inequality</h3>
        <ul>
            <li><strong>Problem:</strong> Crisis costs were disproportionately borne by vulnerable groups</li>
            <li><strong>Lesson:</strong> Financial crises can exacerbate economic inequalities</li>
            <li><strong>Corrective measure:</strong> Policies that consider distributional impacts of crises and bailouts</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with lesson_tabs[4]:  # Persistent Challenges
        st.markdown("""
        <div class="tab-content">
        <h3>Regulatory Effectiveness</h3>
        <ul>
            <li><strong>Challenge:</strong> Avoiding both excessive regulation and imprudent deregulation</li>
            <li><strong>Critical question:</strong> How to calibrate regulation to protect stability without stifling innovation?</li>
        </ul>

        <h3>Financial Innovation</h3>
        <ul>
            <li><strong>Challenge:</strong> New technologies and products create unknown risks</li>
            <li><strong>Critical question:</strong> How to regulate innovations like fintech, cryptocurrencies, and decentralized finance?</li>
        </ul>

        <h3>Emerging Vulnerabilities</h3>
        <ul>
            <li><strong>Challenge:</strong> Risks migrate to less regulated sectors</li>
            <li><strong>Critical question:</strong> How to identify and mitigate new sources of systemic risk?</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Concluding quote
    st.markdown("""
    <div style="margin: 2rem 0; padding: 2rem; text-align: center; background-color: #F3F4F6; border-radius: 10px;">
        <blockquote style="font-size: 1.1rem; font-style: italic; color: #4B5563;">
            "History doesn't repeat itself, but it often rhymes."
            <br><span style="font-size: 0.9rem;">— Attributed to Mark Twain</span>
        </blockquote>
        <p style="margin-top: 1rem;">
        The most important lesson from the subprime crisis may be the constant need for vigilance and humility. 
        Risks in the financial system continuously evolve, requiring regulators, financial institutions, 
        and market participants to adapt their approaches. Financial stability is never permanent - it is a 
        constantly moving target that requires perpetual attention.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Additional resources
    st.markdown('<div class="sub-header">Additional Resources for Study</div>', unsafe_allow_html=True)
    
    # Split into two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Recommended Books
        
        * **"The Crisis of 2008 and the Economics of Depression"** - Paul Krugman
        * **"Too Big to Fail"** - Andrew Ross Sorkin
        * **"The Big Short"** - Michael Lewis
        * **"Lords of Finance"** - Liaquat Ahamed
        * **"This Time Is Different"** - Carmen Reinhart and Kenneth Rogoff
        * **"Crashed: How a Decade of Financial Crises Changed the World"** - Adam Tooze
        """)
    
    with col2:
        st.markdown("""
        ### Documentaries and Movies
        
        * **"Inside Job"** (2010) - Documentary
        * **"The Big Short"** (2015) - Movie
        * **"Margin Call"** (2011) - Movie
        * **"Too Big to Fail"** (2011) - TV Movie
        * **"Frontline: Money, Power and Wall Street"** - Documentary series
        * **"Explained: The 2008 Financial Crisis"** - Netflix
        """)
    
# Footer
st.markdown("""
<div class="footer">
Developed as educational material for financial crisis classes.<br>
© 2025 - Prof. José Américo – Coppead
</div>
""", unsafe_allow_html=True)

# Add CSS to improve the appearance of the application
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