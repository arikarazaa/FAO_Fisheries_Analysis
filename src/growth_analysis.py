# ── Growth/Decline analysis — ISSCAAP group level ─────
# Use species-group level for cleaner signal

from src.config import *
def growth_decline(df_official):
    sp_group_trend = df_official.groupby(['ISSCAAP_Group_En','Year'])['Tonnes'].sum().reset_index()

    # Compare two decades
    decade_old = sp_group_trend[sp_group_trend['Year'].between(2004,2013)] \
        .groupby('ISSCAAP_Group_En')['Tonnes'].mean()
    decade_new = sp_group_trend[sp_group_trend['Year'].between(2014,2023)] \
        .groupby('ISSCAAP_Group_En')['Tonnes'].mean()

    change_df = pd.DataFrame({'Old': decade_old, 'New': decade_new}).dropna()
    change_df['Change_pct'] = (change_df['New'] - change_df['Old']) / change_df['Old'] * 100
    change_df = change_df[change_df['Old'] > 1e5]  # filter out negligible groups
    change_df = change_df.sort_values('Change_pct')

    # Color by direction
    colors_change = ['#f78166' if x < 0 else '#3fb950' for x in change_df['Change_pct']]

    fig, ax = plt.subplots(figsize=(13, 9))
    bars = ax.barh(change_df.index, change_df['Change_pct'],
                color=colors_change, edgecolor='none', height=0.72)

    ax.axvline(0, color='#8b949e', linewidth=1.2)
    ax.set_title('Species Group Catch Change: 2014–2023 vs 2004–2013 (%)',
                fontsize=13, fontweight='bold', pad=14)
    ax.set_xlabel('Change in Average Annual Catch (%)')
    ax.grid(axis='x', alpha=0.3)

    # Legend
    decline_patch = mpatches.Patch(color='#f78166', label='Declining')
    growth_patch  = mpatches.Patch(color='#3fb950',  label='Growing')
    ax.legend(handles=[growth_patch, decline_patch], facecolor='#21262d',
            edgecolor='#30363d', fontsize=9)
    plt.tight_layout()
    plt.savefig('species_decline_growth.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("Biggest declines (% change):")
    print(change_df.nsmallest(5,'Change_pct')[['Old','New','Change_pct']].round(1).to_string())
    print("\nBiggest growth:")
    print(change_df.nlargest(5,'Change_pct')[['Old','New','Change_pct']].round(1).to_string())