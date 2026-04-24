from src.load_data import load_data
from src.preprocess import preprocess

from src.global_analysis import global_trend_analysis
from src.country_analysis import top_countries_analysis
from src.plotly_maps import world_map, continent_animation
from src.species_analysis import species_trends, species_change_plotly
from src.region_analysis import region_stacked, region_ranked
from src.growth_analysis import growth_decline
from src.config import *

def main():
    df_raw, df_countries, df_species, df_areas = load_data()
    df_official = preprocess(df_raw, df_countries, df_species, df_areas)

    global_trend_analysis(df_official)

    recent = top_countries_analysis(df_official)

    world_map(recent, df_countries)

    species_trends(df_official)

    region_stacked(df_official, recent)
    region_ranked(recent)

    growth_decline(df_official)

    species_change_plotly(df_official)

    continent_animation(df_official)

if __name__ == "__main__":
    main()