

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from utils import city_df
import streamlit as st



class FeatureRecommendSimilar:
    """ contains all methods and and attributes needed for recommend using defined feature parameteres """
    
    def __init__(self, city_features: list, number: int, parameter_name) -> None:
        self.city_features = city_features
        self.number = number
        self.top_cities_feature_df = None
        self.first_city = None
        self.feature_countries_df_final = None
        self.parameter_name = parameter_name
        pass

    def calculate_top_cities_for_defined_feature(self):
        """ function that calculates the cities with the highest score with defined parameters.
        It returns: the top city, and a dataframe that contain other cities with similar scores"""
        
        needed_columns = ['city', 'country']
        self.city_features.extend(needed_columns)
        feature_df = city_df.loc[:, self.city_features]
        feature_df.set_index('city', inplace = True)
        feature_df['score'] = feature_df.mean(axis=1)
        self.first_city = feature_df.score.idxmax()
        self.top_cities_feature_df = feature_df.loc[:, ['country','score']].nlargest(self.number, 'score')
        return self.first_city, self.top_cities_feature_df

    
    def aggregate_top_countries(self):
        """ this function gets the aggregate score of all the counties represented in the dataframe  of top cities (self.top_cities_feature_df) """
        feature_countries_df= self.top_cities_feature_df.loc[:, ['country', 'score']]
        feature_countries_df = feature_countries_df.groupby('country').mean()
        self.feature_countries_df_final = feature_countries_df.sort_values('score', ascending=False)
        return self.feature_countries_df_final
    
    def decision_for_predefined_city_features(self):
        """ This function makes recommenddation based on predefined parameters and calculated results"""

        st.markdown('### **Recommendation**')
        st.success(f'Based on your  parameter, **{self.first_city}** is the top recommended city to live or visit.')
        st.write(f'The three features that was used to define {self.parameter_name} city are {self.city_features[0]}, {self.city_features[1]}, {self.city_features[2]}')
        st.markdown('### **Additional info**')
        st.markdown('Below are details of your top city and other similar ones. highest scores is 10')
        final_city_df= pd.DataFrame.reset_index(self.top_cities_feature_df)
        st.table(final_city_df.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        top_countries = pd.DataFrame.reset_index(self.feature_countries_df_final) 
        if len(self.top_cities_feature_df) != len(top_countries) :
            st.markdown('below are the aggregate score of the countries represented in the table of your cities')
            st.table(top_countries.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        else:
            pass
        pass
        st.write(f" PS: you can also choose features to define your own city. To do this, pick the option 'define your parmeter for a desired' city above")
        

    def decision_for_user_defined_city(self):
        """ This function makes recommenddation based on selected features and calculated results"""

        st.markdown('### **Recommendation**')
        if self.parameter_name != '':
            st.success(f'Based on your  parameter ({self.parameter_name}), **{self.first_city}** is the top recommended city to live or visit.')
        else:
            st.success(f'Based on your  parameter, **{self.first_city}** is the top recommended city to live or visit.')
        st.markdown('### **Additional info**')
        st.markdown('Below are details of your top city and other similar ones. highest scores is 10')
        final_city_df= pd.DataFrame.reset_index(self.top_cities_feature_df)
        st.table(final_city_df.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        top_countries = pd.DataFrame.reset_index(self.feature_countries_df_final) 
        if len(self.top_cities_feature_df) != len(top_countries) :
            st.markdown('below are the aggregate score of the countries represented in the table of your cities')
            st.table(top_countries.style.format({'score':'{:17,.1f}'}).background_gradient(cmap='Greens').set_properties(subset=['score'], **{'width': '250px'}))
        else:
            pass

    


