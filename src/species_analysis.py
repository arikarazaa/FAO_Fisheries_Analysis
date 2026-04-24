
from src.config import *
def species_trends(df_official):

# ── Species trend lines — 6 key species ───────────────
    key_species = [
        'Anchoveta(=Peruvian anchovy)',
        'Atlantic cod',
        'Atlantic herring',
        'Alaska pollock(=Walleye poll.)',
        'Yellowfin tuna',
        'Blue whiting(=Poutassou)',
    ]

    sp_trend = df_official[df_official['Species'].isin(key_species)] \
        .groupby(['Species','Year'])['Tonnes'].sum().reset_index()
    sp_trend['Mt'] = sp_trend['Tonnes'] / 1e6

    colors_sp = ['#f0883e','#f78166','#58a6ff','#3fb950','#d2a8ff','#ffa657']

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    axes = axes.flatten()

    for i, (sp, col) in enumerate(zip(key_species, colors_sp)):
        subset = sp_trend[sp_trend['Species'] == sp].sort_values('Year')
        ax = axes[i]
        ax.fill_between(subset['Year'], subset['Mt'], alpha=0.15, color=col)
        ax.plot(subset['Year'], subset['Mt'], color=col, linewidth=2)

        peak_row = subset.loc[subset['Mt'].idxmax()]
        ax.axvline(peak_row['Year'], color=col, linewidth=0.8, linestyle='--', alpha=0.6)
        ax.text(peak_row['Year'] + 1, subset['Mt'].max() * 0.92,
                f"Peak {int(peak_row['Year'])}", fontsize=7.5, color=col)

        short_name = sp.split('(')[0].strip()
        ax.set_title(short_name, fontsize=10, fontweight='bold', color=col)
        ax.set_xlabel('Year', fontsize=8)
        ax.set_ylabel('Mt', fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.tick_params(labelsize=8)

    fig.suptitle('Catch Trends for Six Commercially Important Species (1950–2023)',
                fontsize=13, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig('species_trends.png', dpi=150, bbox_inches='tight')
    plt.show()

    
    
# ── Interactive Plotly: individual species % change ────
def species_change_plotly(df_official):  
    
    sp_old = df_official[df_official['Year'].between(2004,2013)] \
        .groupby('Species')['Tonnes'].mean()
    sp_new = df_official[df_official['Year'].between(2014,2023)] \
        .groupby('Species')['Tonnes'].mean()

    sp_change = pd.DataFrame({'Old':sp_old,'New':sp_new}).dropna()
    sp_change = sp_change[sp_change['Old'] > 5e4]  # meaningful size only
    sp_change['Change_pct'] = (sp_change['New'] - sp_change['Old']) / sp_change['Old'] * 100
    sp_change['Direction'] = sp_change['Change_pct'].apply(lambda x: 'Declining' if x<0 else 'Growing')
    sp_change['AbsChange'] = sp_change['Change_pct'].abs()

    top_sp_change = pd.concat([
        sp_change[sp_change['Direction']=='Declining'].nsmallest(15,'Change_pct'),
        sp_change[sp_change['Direction']=='Growing'].nlargest(15,'Change_pct')
    ]).reset_index()

    fig = px.bar(
        top_sp_change.sort_values('Change_pct'),
        x='Change_pct', y='Species',
        color='Direction',
        color_discrete_map={'Declining':'#f78166','Growing':'#3fb950'},
        orientation='h',
        title='Top 15 Growing & Declining Species — Catch Change (2014–2023 vs 2004–2013)',
        labels={'Change_pct': '% Change in Avg Annual Catch'},
        hover_data={'Old':':.0f','New':':.0f'}
    )
    fig.update_layout(
        height=700,
        paper_bgcolor='#0d1117', plot_bgcolor='#161b22',
        font=dict(color='#c9d1d9'),
        title_font_size=13,
        yaxis=dict(tickfont=dict(size=10)),
        legend=dict(bgcolor='#21262d')
    )
    fig.add_vline(x=0, line_color='#8b949e', line_width=1.2)
    fig.show()