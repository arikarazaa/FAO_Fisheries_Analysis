
from src.config import *

def world_map(recent, df_countries):
# ── Choropleth world map using Plotly ──────────────────
# Aggregate by country and get ISO codes
    country_totals = recent.merge(
        df_countries[['UN_Code','ISO3_Code','Name_En']],
        left_on='COUNTRY.UN_CODE', right_on='UN_Code', how='left'
    ).groupby(['ISO3_Code','Name_En'])['Tonnes'].sum().reset_index()
    country_totals['Mt'] = country_totals['Tonnes'] / 1e6

    fig = px.choropleth(
        country_totals,
        locations='ISO3_Code',
        color='Mt',
        hover_name='Name_En',
        hover_data={'Mt': ':.1f', 'ISO3_Code': False},
        color_continuous_scale='YlOrRd',
        range_color=[0, country_totals['Mt'].quantile(0.97)],  # cap scale at 97th pct for readability
        title='Total Capture Production by Country (2015–2023, Million Tonnes)',
        labels={'Mt': 'Million Tonnes'}
    )
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True, coastlinecolor='#444'),
        paper_bgcolor='#0d1117',
        plot_bgcolor='#0d1117',
        font=dict(color='#c9d1d9'),
        title_font_size=14,
        coloraxis_colorbar=dict(title='Mt', tickfont=dict(color='#8b949e'))
    )
    fig.show()
    
    
def continent_animation(df_official):

# ── Continent share over time — animated Plotly bubble ─
    continent_year = df_official.groupby(['Continent_Group_En','Year'])['Tonnes'].sum().reset_index()
    continent_year['Mt'] = continent_year['Tonnes'] / 1e6
    continent_year = continent_year.dropna(subset=['Continent_Group_En'])

    fig = px.bar(
        continent_year[continent_year['Year'].isin(range(1955,2024,5))],
        x='Continent_Group_En', y='Mt',
        animation_frame='Year',
        color='Continent_Group_En',
        title='Capture Production by Continent — Every 5 Years (1955–2020)',
        labels={'Mt':'Million Tonnes','Continent_Group_En':'Continent'},
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_layout(
        height=480,
        paper_bgcolor='#0d1117', plot_bgcolor='#161b22',
        font=dict(color='#c9d1d9'),
        showlegend=False,
        title_font_size=13,
        yaxis=dict(range=[0, continent_year['Mt'].max()*1.15])
    )
    fig.show()