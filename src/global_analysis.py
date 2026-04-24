# ── Global production trend ────────────────────────────

from src.config import *
def global_trend_analysis(df_official):
    global_trend = df_official.groupby('Year')['Tonnes'].sum().reset_index()
    global_trend['Mt'] = global_trend['Tonnes'] / 1e6   # convert to million tonnes

    fig, ax = plt.subplots(figsize=(14, 5))

    # Area fill
    ax.fill_between(global_trend['Year'], global_trend['Mt'], alpha=0.18, color='#58a6ff')
    ax.plot(global_trend['Year'], global_trend['Mt'], color='#58a6ff', linewidth=2.2)

    # Annotate peak
    peak_row = global_trend.loc[global_trend['Mt'].idxmax()]
    ax.annotate(
        f"Peak: {peak_row['Mt']:.1f} Mt ({int(peak_row['Year'])})",
        xy=(peak_row['Year'], peak_row['Mt']),
        xytext=(peak_row['Year'] - 12, peak_row['Mt'] + 2),
        arrowprops=dict(arrowstyle='->', color='#f78166', lw=1.5),
        color='#f78166', fontsize=10, fontweight='bold'
    )

    # Shade "plateau era"
    ax.axvspan(1994, 2023, alpha=0.07, color='#f0883e', label='Post-peak plateau (1994–present)')
    ax.axhline(y=global_trend['Mt'].mean(), color='#3fb950', linewidth=1, linestyle='--', label=f"Historical average ({global_trend['Mt'].mean():.1f} Mt)")

    ax.set_title('Global Marine & Inland Capture Production (1950–2023)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Year')
    ax.set_ylabel('Production (Million Tonnes)')
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.0f Mt'))
    ax.legend(facecolor='#21262d', edgecolor='#30363d', fontsize=9)
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('global_trend.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"\nGlobal production grew from {global_trend[global_trend['Year']==1950]['Mt'].values[0]:.1f} Mt (1950) to a peak of {peak_row['Mt']:.1f} Mt ({int(peak_row['Year'])})")
    print(f"By 2023 it had settled at {global_trend[global_trend['Year']==2023]['Mt'].values[0]:.1f} Mt — roughly where it was in the early 1990s.")