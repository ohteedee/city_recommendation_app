import streamlit as st
from PIL import Image
from utils import  generate_city_list
from recommender import FeatureRecommendSimilar, CosineRecommendSimilar






# import time 
# import numpy as np

# from utils import load_data





# The app controller
def app():

    navigation = st.sidebar.radio('contents', ('main app', 'about'))

    st.sidebar.write('app designed by Tosin D. Oyewale (Ph.D)')
    st.sidebar.write('Linkedin - https://www.linkedin.com/in/tosin-oyewale/')
    st.sidebar.write('email- tosinoyewale@yahoo.co.uk')

    if navigation == 'main app':

        st.title("Ohteedee's city recommender application")
        st.write('This application recomends cities that are similar to your current city so that you can visit or live')

        img= Image.open('picture/city1.jpeg')
        st.image(img, use_column_width=True)
    

        model_choice = st.radio('Please, select one of the options below',
                                ('look for city similar you like or live', 'look for certain parameters in a city'))
        
        if model_choice == 'look for city similar to one I like':

            city_list = generate_city_list()
            city_choice = st.selectbox("Select a city of you liked or live", (city_list))
            if city_choice != "none":
                liked_city = city_choice.split(',')[0]
                
                user_input = CosineRecommendSimilar(liked_city) 
                liked_city_closest, other_close_cities_df = user_input.cosine_using_city_I_like()
                st.success(f'The city that is most cimilar to the city you chose is {liked_city_closest}')
                st.subheader('Below are other similar cities and their scores out of 10')
                st.dataframe(other_close_cities_df)

        elif model_choice == 'look for certain parameters in a city':
            pass
    

    # city_df, data, city_scores, location = load_data()
    # location.append('Others')
    # city = st.selectbox("Location of Residence", location)
    # city_choice = st.multiselect("Choose the 5 features that matters to you the most in a city",city_scores.columns)
    # if st.checkbox("Rate the features"):
    #      if len(city_choice) == 5 :
    #         rating1 = st.number_input(city_choice[0], 1,10, step=1)
    #         rating2 = st.number_input(city_choice[1], 1,10, step=1)
    #         rating3 = st.number_input(city_choice[2], 1,10, step=1)
    #         rating4 = st.number_input(city_choice[3], 1,10, step=1)
    #         rating5 = st.number_input(city_choice[4], 1,10, step=1)

    #         if st.button("Recommend", key="hi"):
    #             user = np.array([rating1, rating2,rating3,rating4,rating5])
    #             column = city_choice
    #             number = len(city_choice)
    #             input = CosineRecommendCity(column, user, number, city, city_scores, city_df, data)
    #             city_similar = input.reccommend_city()
    #             with st.spinner("Analysing..."):
    #                 time.sleep(5)
    #             st.text(f'\n\n\n')
    #             st.subheader(' This is your recommendation')
    #             st.text(f'\n\n\n\n\n\n')
    #             st.success(f'Based on your city coices and ratings, you may want to explore a city like {city_similar}.')
    #             country , subtitle, response, breakdown = input.get_city_info()
    #             st.text(f'\n\n\n\n\n\n')
    #             st.write(f'{city_similar} is a city in {country}. {response}')
    #             st.text(subtitle)
    #             st.table(breakdown.style.format({'Score':'{:17,.1f}'}).background_gradient(cmap='Blues').set_properties(subset=['Score'], **{'width': '250px'}))
    #             st.markdown(f'For more info on  the original data sourrce and city ranks, see [here](https://www.nestpick.com/millennial-city-ranking-2018/)')


    #      elif len(city_choice) > 5:
    #           st.warning("choose only 5 features")
    #      else:
    #          st.error("You are to choose at least 5 feature from the bove options")
  
    

if __name__ == "__main__":
    app()
