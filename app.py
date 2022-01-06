import streamlit as st
from PIL import Image
import pandas as pd
import time 
from utils import  generate_city_list, get_feature_list
from recomenders.feature_recommender import FeatureRecommendSimilar
from recomenders.cosine_recommender import CosineRecommendSimilar



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
    

        model_choice = st.radio( ' Please, select one of the options below',
                                ('none','look for city similar you like or live', 'look for certain parameters in a city'))
        
        if model_choice == 'none':
            pass
        
        elif model_choice == 'look for city similar you like or live':
            st.subheader(" ")
            st.subheader('select a city ')
            form = st.form(key='my-form')
            city_list = generate_city_list()
            city_list.append(' none')
            city_choice = form.selectbox("Select a city you liked or live", city_list)
            submit = form.form_submit_button('check for silimar city')
            if submit:
                liked_city = city_choice.split(',')[0]
                user_input_cosine = CosineRecommendSimilar(liked_city) 
                user_input_cosine.cosine_using_city_I_like()
                user_input_cosine.decision_for_liked_city()
                # st.success(f'The city that is most cimilar to the city you chose is {liked_city_closest}')
                # st.subheader('Below are other similar cities and their scores out of 10')
                # st.dataframe(other_close_cities_df)

        elif model_choice == 'look for certain parameters in a city':
            
            st.subheader(" ")

            parameter_option = st.radio( 'please select one of the options',
                                ('none','use a pre-defined parameter', 'define your parmeter for a desired city'))
            if parameter_option != 'none':
                if parameter_option == 'use a pre-defined parameter':
                    st.subheader('What parameter would you like to use to search for cities')
                    form = st.form(key='my-form')
                    social = form.checkbox('look for city with high social life')
                    business = form.checkbox('look for city with thriving business ecosystems')
                    female_friendly = form.checkbox('look for city that are female friendly')
                    number = form.text_input('type the number of cities you want to see here', value = 20)
                    submit = form.form_submit_button('seacrh for cities')
                    
                    
                    if submit:
                        if social:
                            pass
                        elif business:
                            pass
                        else:
                            female_friendly
                
                
                elif parameter_option == 'define your parmeter for a desired city':
                    st.subheader(' ')
                    st.markdown('you can define your desired city with the form below')
                    form = st.form(key='my-form')
                    parameter_name = form.text_input('please type the name of parameter you would like to search (optional)' )
                    list_of_features = get_feature_list()
                    parameter_fearture = form.multiselect( 'select as many features that defines your desired city',  list_of_features)
                    number = form.text_input('type the number of cities you want to see here', value = 20)
                    submit = form.form_submit_button('seacrh for cities' )

                    if submit:

                        if parameter_fearture == []:
                            st.warning('you must select an a city feature')
                        else:
                    
                            try:
                                number = int(number)
                                if number == 0:
                                    st.warning('number must be greater than 0')
                                elif number <= 100 :
                                    user_input_feature2 = FeatureRecommendSimilar(parameter_fearture, number, parameter_name)
                                    user_input_feature2.calculate_top_cities_for_defined_feature()
                                    user_input_feature2.top_countries_based_on_selected_cities()
                                    with st.spinner("Analysing..."):
                                        time.sleep(2)
                                        user_input_feature2.decision_for_personally_defined_city()
                                else:
                                    st.warning('number must be less than 100')
                            except ValueError:
                                st.warning('that was not a valid number. try again')

                        


                       


                    
    

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
