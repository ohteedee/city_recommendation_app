 
import pandas as pd
 
city_df = pd.read_csv('data/city_ranking.csv')

def generate_city_list():
    location = []
    for index, city, country in city_df[["city", "country"]].sort_values("city").itertuples():
        new = f'{city}, {country}'
        location.append(new)
    return location 



