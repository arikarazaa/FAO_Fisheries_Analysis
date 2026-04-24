# preprocess.py

from src.config import *

def preprocess(df_raw, df_countries, df_species, df_areas):

    df = df_raw.merge(
        df_countries[['UN_Code','Name_En','Continent_Group_En','GeoRegion_Group_En']],
        left_on='COUNTRY.UN_CODE', right_on='UN_Code', how='left'
    )

    df = df.merge(
        df_species[['3A_Code','Name_En','ISSCAAP_Group_En','Major_Group']],
        left_on='SPECIES.ALPHA_3_CODE', right_on='3A_Code', how='left',
        suffixes=('_country','_species')
    )

    df = df.merge(
        df_areas[['Code','Name_En','FARegion_Group_En','InlandMarine_Group_En','Ocean_Group_En']],
        left_on='AREA.CODE', right_on='Code', how='left'
    )

    df.rename(columns={
        'Name_En_country':  'Country',
        'Name_En_species':  'Species',
        'Name_En':          'FishingArea',
        'PERIOD':           'Year',
        'VALUE':            'Tonnes'
    }, inplace=True)

    df_official = df[df['STATUS'].isin(['A','E'])].copy()

    print(f"Rows after quality filter: {len(df_official):,}")
    print(df_official[['Country','Species','FishingArea','Year','Tonnes']].head(3))

    return df_official