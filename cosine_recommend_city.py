

import pandas as pd
from utils import load_data
from sklearn.metrics.pairwise import cosine_similarity


city_df, data, city_scores, location = load_data()


class CosineRecommendCity:
    def __init__(self, column, user, number, city, city_scores, city_df, data) -> None:
        self.column = column
        self.user = user
        self.number = number
        self.city = city
        self.city_df = city_df
        self.data = data
        self.city_scores = city_scores
        self.city_similar = None

        pass

   

    #Calculate how similar using cosine_similarity
    def reccommend_city(self):
        if self.city == 'Others':
            new_df = self.city_scores[self.column]
        else:
            locate = self.city.split(',')
            new_df = self.city_scores[self.city_scores.index !=  locate[0]][self.column]
        value = []
        for index,city in enumerate(new_df.index):
            city_old = new_df.loc[city].values.reshape(-1, self.number)
            user1 = self.user.reshape(-1, self.number)
            score = cosine_similarity(city_old, user1)
            value.append(score)
        similarity = pd.Series(value, index=new_df.index)
        self.city_similar = similarity.sort_values(ascending=False).astype(float).idxmax()
        return self.city_similar

    # Get more info about the recommended city
    def get_city_info(self):
        subtitle = 'City Ranking in terms of Business, essentials, Openness and recreation scores(over 10.0)'
        country = self.city_df.loc[self.city_df['city'] == self.city_similar, 'country'].iloc[0]
        if self.city_similar in self.city_df['city'].head().values:
            response = "It is actually one of the top 5 cities that has piqued millennials' interests."
        elif self.city_similar in self.city_df['city'].head(10).values:
            response = "It is actually one of the top 10 cities that has piqued millennials' interests."
        elif self.city_similar in self.city_df['city'].tail(5).values:
            response = "It is actually one of the least 5 cities that has piqued millennials' interests."
        else:
            response = ""

        ranking = list(zip(list(self.data.loc[self.city_similar].index),self.data.loc[self.city_similar]))
        breakdown = pd.DataFrame(ranking, columns = ['Category','Score'])
        breakdown['Score'] = breakdown['Score'].round(1)

        return country , subtitle, response, breakdown




        def cosine_using_city_I_like(liked_city: str):
            vector_df =city_df.set_index('city').drop(columns = ['country', 'Total'])
            similarity = cosine_similarity(vector_df)
            similarity_df = pd.DataFrame(similarity, index = vector_df.index, columns = vector_df.index)
            liked_city_closest = similarity_df.loc[liked_city].drop(labels = [liked_city]).idxmax()
            other_close_cities = similarity_df.loc[liked_city].drop(labels = [liked_city]).sort_values(ascending = False).iloc[1:6]
            other_close_cities_df = pd.DataFrame(data=other_close_cities)
            other_close_cities_df = other_close_cities_df.rename(columns = {liked_city:'other_similar_citties'})
            return liked_city_closest, other_close_cities_df
