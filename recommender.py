

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from utils import city_df

class FeatureRecommendSimilar:
    
    def __init__(self, city_features: list, number: int) -> None:
        self.city_features = city_features
        self.number = number
        self.top_city_feature_df = None
        
        pass

    def calculate_top_cities_for_defined_feature(self):

        feature_df = city_df.loc[:, self.city_features]
        feature_df.set_index('city', inplace = True)
        feature_df['score'] = feature_df.mean(axis=1)
        city_feature_df = feature_df.sort_values('score', ascending = False)
        top_city_feature_df = city_feature_df.loc[:, ['country','score']].head(self.number)
        return self.top_city_feature_df

    def top_countries_based_selected_cities(self):
        feature_countries_df= self.top_city_feature_df.loc[:, ['country', 'score']]
        feature_countries_df = feature_countries_df.groupby('country').mean()
        feature_countries_df = feature_countries_df.sort_values('score', ascending=False)
        return feature_countries_df



class CosineRecommendSimilar:
    
    def __init__(self,liked_city: str) -> None:
     
        self.liked_city = liked_city
        pass

    def cosine_using_city_I_like(self):
                vector_df =city_df.set_index('city').drop(columns = ['country', 'Total'])
                similarity = cosine_similarity(vector_df)
                similarity_df = pd.DataFrame(similarity, index = vector_df.index, columns = vector_df.index)
                liked_city_closest = similarity_df.loc[self.liked_city].drop(labels = [self.liked_city]).idxmax()
                other_close_cities = similarity_df.loc[self.liked_city].drop(labels = [self.liked_city]).sort_values(ascending = False).iloc[1:6]
                other_close_cities_df = pd.DataFrame(data=other_close_cities)
                other_close_cities_df = other_close_cities_df.rename(columns = {self.liked_city:'other_similar_citties'})
                return liked_city_closest, other_close_cities_df
