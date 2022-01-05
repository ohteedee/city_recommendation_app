from utils import load_data

city_df, data, city_scores, location =load_data()

def calculate_top_cities_for_defined_feature(features: list, n: int):
    feature_df = city_df.loc[:, features]
    feature_df.set_index('city', inplace = True)
    feature_df['score'] = feature_df.mean(axis=1)
    city_feature_df = feature_df.sort_values('score', ascending = False)
    top_city_feature_df = city_feature_df.loc[:, ['country','score']].head(n)
    return top_city_feature_df

def top_countries_based_selected_cities(top_city_feature_df):
    feature_countries_df= top_city_feature_df.loc[:, ['country', 'score']]
    feature_countries_df = feature_countries_df.groupby('country').mean()
    feature_countries_df = feature_countries_df.sort_values('score', ascending=False)
    return feature_countries_df