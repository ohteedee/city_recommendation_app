 
import pandas as pd
 
city_df = pd.read_csv('data/city_ranking.csv')

def city_country_list():
    location = []
    for index, city, country in city_df[["city", "country"]].itertuples():
        new = f'{city}, {country}'
        location.append(new)
    return location 


def load_data():
    
    data = city_df.set_index('city').iloc[:,1:-1]
    city_scores = city_df.set_index('city').iloc[:,1:-1].round().astype(int)
    
    return city_df, data, city_scores,
