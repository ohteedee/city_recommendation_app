 
import pandas as pd
 
city_df = pd.read_csv('data/city_ranking.csv')

def generate_city_list():
    """ This funtion generates the list of city, country fron dataframe city_df  """
    
    location = []
    for index, city, country in city_df[["city", "country"]].sort_values("city").itertuples():
        new = f'{city}, {country}'
        location.append(new)
    return location 

def get_feature_list():
    """ This funtion generates the list of all the features used to describe city in dataframe city_df  """

    feature_list = city_df.columns[2:-1]
    return feature_list




