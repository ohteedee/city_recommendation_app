

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from utils import city_df
import streamlit as st



class FeatureRecommendSimilar:
    """ fill later """
    
    def __init__(self, city_features: list, number: int, parameter_name) -> None:
        self.city_features = city_features
        self.number = number
        self.top_cities_feature_df = None
        self.first_city = None
        self.feature_countries_df_final = None
        self.parameter_name = parameter_name
        pass

    def calculate_top_cities_for_defined_feature(self):
        """ fill later """
        
        needed_columns = ['city', 'country']
        self.city_features.extend(needed_columns)
        feature_df = city_df.loc[:, self.city_features]
        feature_df.set_index('city', inplace = True)
        feature_df['score'] = feature_df.mean(axis=1)
        city_feature_df = feature_df.sort_values('score', ascending = False)
        self.first_city = city_feature_df.score.idxmax()
        self.top_cities_feature_df = city_feature_df.loc[:, ['country','score']].head(self.number)
        return self.first_city, self.top_cities_feature_df

    
    def top_countries_based_on_selected_cities(self):
        """ fill later """
        feature_countries_df= self.top_cities_feature_df.loc[:, ['country', 'score']]
        feature_countries_df = feature_countries_df.groupby('country').mean()
        self.feature_countries_df_final = feature_countries_df.sort_values('score', ascending=False)
        return self.feature_countries_df_final
    
    
    def decision_for_personally_defined_city(self):
        """ fill later """

        st.markdown('----------------------------------------------------------**Recommendation**----------------------------------------------------------')
        st.markdown(f'Based on your  parameter, **{self.first_city}** is the top recommended city to live or visit.')
        st.markdown('------------------------------------------------------------**Additional info**------------------------------------------------------------')
        st.markdown('Below are details of your top city and other similar ones. highest scores is 10')
        final_city_df= pd.DataFrame.reset_index(self.top_cities_feature_df)
        st.table(final_city_df.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        top_countries = pd.DataFrame.reset_index(self.feature_countries_df_final) 
        if len(self.top_cities_feature_df) != len(top_countries) :
            st.markdown('below are the aggregate score of the countries represented in the table of your cities')
            st.table(top_countries.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        else:
            pass

