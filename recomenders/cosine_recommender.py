
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from utils import city_df
import streamlit as st


class CosineRecommendSimilar:
    """ fill later """
    
    def __init__(self,liked_city: str) -> None:
     
        self.liked_city = liked_city
        self.liked_city_closest = None
        self.other_close_cities_df = None
        pass

    def cosine_using_city_I_like(self):

        """ fill later """

        vector_df =city_df.set_index('city').drop(columns = ['country', 'Total'])
        similarity = cosine_similarity(vector_df)
        similarity_df = pd.DataFrame(similarity, index = vector_df.index, columns = vector_df.index)
        self.liked_city_closest = similarity_df.loc[self.liked_city].drop(labels = [self.liked_city]).idxmax()
        other_close_cities = similarity_df.loc[self.liked_city].drop(labels = [self.liked_city]).sort_values(ascending = False).iloc[1:6]
        self.other_close_cities_df = pd.DataFrame(data=other_close_cities)
        self.other_close_cities_df = self.other_close_cities_df.rename(columns = {self.liked_city:'other_similar_citties'})
        return self.liked_city_closest, self.other_close_cities_df


    def decision_for_liked_city(self):
        """  fill later """
        st.success(f'The city that is most cimilar to the city you chose is {self.liked_city_closest}')
        st.subheader('Below are other similar cities and their scores out of 0 to 1')
        self.other_close_cities_df = pd.DataFrame.reset_index(self.other_close_cities_df)
        st.table(self.other_close_cities_df.style.format({'other_similar_citties':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['other_similar_citties'], **{'width': '250px'}))
        