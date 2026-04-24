# ── Top 15 countries — horizontal bar (2015-2023) ──────

from src.config import *
def top_countries_analysis(df_official):
    recent = df_official[df_official['Year'] >= 2015]
    top15 = recent.groupby('Country')['Tonnes'].sum().nlargest(15).reset_index()
    top15['Mt'] = top15['Tonnes'] / 1e6
    top15 = top15.sort_values('Mt')

    # Color gradient
    colors = plt.cm.YlOrRd(np.linspace(0.35, 0.95, len(top15)))

    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.barh(top15['Country'], top15['Mt'], color=colors, edgecolor='none', height=0.7)

    for bar, val in zip(bars, top15['Mt']):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{val:.1f} Mt', va='center', fontsize=9, color='#c9d1d9')

    ax.set_title('Top 15 Fishing Nations — Cumulative Catch (2015–2023)', fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel('Total Catch (Million Tonnes)')
    ax.grid(axis='x', alpha=0.4)
    ax.set_xlim(0, top15['Mt'].max() * 1.15)
    plt.tight_layout()
    plt.savefig('top_countries_bar.png', dpi=150, bbox_inches='tight')
    plt.show()
    return recent  