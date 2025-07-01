import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import numpy as np
import uuid

# Load the dataset
df = pd.read_csv('2015.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("World Happiness Report 2015 Dashboard", style={'textAlign': 'center', 'marginBottom': '20px'}),
    
    # Tabs for different visualizations
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Top & Bottom Happy Countries', value='tab-1'),
        dcc.Tab(label='Money & Happiness', value='tab-2'),
        dcc.Tab(label='Regional Comparison', value='tab-3'),
        dcc.Tab(label='Freedom Effect', value='tab-4'),
        dcc.Tab(label='Secret Sauce Leaders', value='tab-5'),
    ]),
    
    html.Div(id='tabs-content', style={'padding': '20px'})
])

# Callback to render content based on selected tab
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        # Top 10 happiest and least happy countries
        top_10 = df.nlargest(10, 'Happiness Score')
        bottom_10 = df.nsmallest(10, 'Happiness Score')
        combined = pd.concat([top_10, bottom_10])
        combined['Group'] = ['Top 10'] * 10 + ['Bottom 10'] * 10
        
        fig = px.bar(
            combined,
            x='Happiness Score',
            y='Country',
            color='Group',
            title='Top 10 Happiest vs. Least Happy Countries',
            orientation='h',
            height=600
        )
        fig.update_layout(
            yaxis={'categoryorder': 'total ascending'},
            showlegend=True,
            margin={'l': 150}
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])
    
    elif tab == 'tab-2':
        # Correlation heatmap
        corr_cols = ['Happiness Score', 'Economy (GDP per Capita)', 'Family', 
                    'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 
                    'Generosity']
        corr_matrix = df[corr_cols].corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmin=-1,
            zmax=1,
            text=np.round(corr_matrix.values, 2),
            texttemplate="%{text}",
            textfont={"size": 10}
        ))
        fig.update_layout(
            title='Correlation Heatmap: Happiness Score & Contributing Factors',
            height=600,
            width=700
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])
    
    elif tab == 'tab-3':
        # Regional comparison
        regional_avg = df.groupby('Region').agg({
            'Happiness Score': 'mean',
            'Trust (Government Corruption)': 'mean'
        }).reset_index()
        
        fig = px.bar(
            regional_avg,
            x='Region',
            y=['Happiness Score', 'Trust (Government Corruption)'],
            barmode='group',
            title='Average Happiness Score and Trust by Region',
            height=600
        )
        fig.update_layout(
            xaxis_tickangle=45,
            yaxis_title='Score',
            legend_title='Metric'
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])
    
    elif tab == 'tab-4':
        # Freedom vs Happiness scatter plot
        fig = px.scatter(
            df,
            x='Freedom',
            y='Happiness Score',
            color='Region',
            hover_data=['Country'],
            title='Freedom vs. Happiness Score',
            height=600
        )
        fig.update_layout(
            showlegend=True
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])
    
    elif tab == 'tab-5':
        # Leaders in individual factors
        factors = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 
                  'Freedom', 'Trust (Government Corruption)', 'Generosity']
        leaders = []
        for factor in factors:
            top_country = df.loc[df[factor].idxmax(), ['Country', factor]]
            leaders.append({
                'Factor': factor,
                'Country': top_country['Country'],
                'Score': round(top_country[factor], 3)
            })
        leaders_df = pd.DataFrame(leaders)
        
        fig = px.bar(
            leaders_df,
            x='Factor',
            y='Score',
            color='Country',
            title='Top Countries by Individual Happiness Factors',
            text='Country',
            height=600
        )
        fig.update_layout(
            xaxis_tickangle=45,
            showlegend=False
        )
        
        return html.Div([
            dcc.Graph(figure=fig)
        ])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)  # ✅ this is the correct method now
