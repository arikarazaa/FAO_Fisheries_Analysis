# load_data.py
# ── Load all reference tables ──────────────────────────
from src.config import *
def load_data():
    df_raw      = pd.read_csv('data/Capture_Quantity.csv')
    df_countries = pd.read_csv('data/CL_FI_COUNTRY_GROUPS.csv')
    df_species   = pd.read_csv('data/CL_FI_SPECIES_GROUPS.csv')
    df_areas     = pd.read_csv('data/CL_FI_WATERAREA_GROUPS.csv')

    print(f"Capture records loaded : {len(df_raw):,}")
    print(f"Countries in reference : {len(df_countries)}")
    print(f"Species in reference   : {len(df_species):,}")
    print(f"Water areas in reference: {len(df_areas)}")
    print(f"\nYear range : {df_raw['PERIOD'].min()} – {df_raw['PERIOD'].max()}")


    return df_raw, df_countries, df_species, df_areas