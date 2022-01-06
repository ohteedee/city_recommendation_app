 
import pandas as pd
 
city_df = pd.read_csv('data/city_ranking.csv')

def generate_city_list():
    """ fill later """
    
    location = []
    for index, city, country in city_df[["city", "country"]].sort_values("city").itertuples():
        new = f'{city}, {country}'
        location.append(new)
    return location 

def get_feature_list():
    """ fill later """

    list1 = city_df.columns
    feature_list = list1[2:-1]
    return feature_list



