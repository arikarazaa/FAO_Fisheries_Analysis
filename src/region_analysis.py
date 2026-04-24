# ── Top fishing regions — stacked area chart ──────────

from src.config import *
def region_stacked(df_official, recent):
    top_area_names = recent.groupby('FishingArea')['Tonnes'].sum() \
        .nlargest(8).index.tolist()

    area_time = df_official[df_official['FishingArea'].isin(top_area_names)] \
        .groupby(['FishingArea','Year'])['Tonnes'].sum().reset_index()
    area_time['Mt'] = area_time['Tonnes'] / 1e6

    pivot = area_time.pivot(index='Year', columns='FishingArea', values='Mt').fillna(0)

    palette = ['#58a6ff','#3fb950','#f0883e','#d2a8ff',
            '#ffa657','#f78166','#79c0ff','#56d364']

    fig, ax = plt.subplots(figsize=(15, 6))
    ax.stackplot(pivot.index, [pivot[col] for col in pivot.columns],
                labels=pivot.columns, colors=palette, alpha=0.85)

    ax.set_title('Capture Production by Top Fishing Regions — Stacked Area (1950–2023)',
                fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (Million Tonnes)')
    ax.legend(loc='upper left', fontsize=7.5, facecolor='#21262d',
            edgecolor='#30363d', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('regions_stacked.png', dpi=150, bbox_inches='tight')
    plt.show()

# ── Ranked bar chart for recent era ────────────────────

def region_ranked(recent):
    region_recent = recent.groupby('FishingArea')['Tonnes'].sum().nlargest(12).reset_index()
    region_recent['Mt'] = region_recent['Tonnes'] / 1e6
    region_recent = region_recent.sort_values('Mt', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(region_recent['FishingArea'], region_recent['Mt'],
                color='#58a6ff', edgecolor='none', height=0.65)
    for bar, val in zip(bars, region_recent['Mt']):
        ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height()/2,
                f'{val:.0f} Mt', va='center', fontsize=8.5, color='#c9d1d9')

    ax.set_title('Ranked Fishing Regions by Total Catch (2015–2023)', fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('Million Tonnes')
    ax.set_xlim(0, region_recent['Mt'].max() * 1.15)
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('regions_ranked.png', dpi=150, bbox_inches='tight')
    plt.show()