import streamlit as st
from PIL import Image
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
        st.title("ohteedee city recommender app")
        img= Image.open('picture/city1.jpeg')
        st.image(img, use_column_width=True)

        html_code = """
        <div style="background-color:#91e6bf;padding:2px">
        <p><b>city_recommendation_app</b>  is web-app that can recommend cities for people to either <b>live or visitfor touristic purposes</b> . 
        The app was designed using a 2018 city ranking dataset generated by <b>NestPick</b>. The ranking was done primarilly by <b>millenials</b> . 
        The original data which I explored and used to generate the app can be found <a href="https://www.nestpick.com/millennial-city-ranking-2018/">here</a> </p>
        </div>
        <br>
        """
    
        st.markdown(html_code, unsafe_allow_html=True)
    
        model_choice = st.radio( ' Please, select one of the options below',
                                ('none','look for city similar to the one you like or live', 'look for certain parameters in a city'))
        
        if model_choice == 'none':
            pass
        
        elif model_choice == 'look for city similar to the one you like or live':
            st.subheader(" ")
            st.subheader('select a city ')
            form = st.form(key='my-form')
            city_list = generate_city_list()
            city_list.append(' none')
            city_choice = form.selectbox("Select a city you liked or live", city_list)
            submit = form.form_submit_button('check for silimar city')
            if submit:
                with st.spinner("Analysing..."):
                    time.sleep(2)
                    liked_city = city_choice.split(',')[0]
                    user_input_cosine = CosineRecommendSimilar(liked_city) 
                    user_input_cosine.cosine_using_city_I_like()
                    
                    main_comment, side_comment = user_input_cosine.comment_for_closest_city()
                    st.success(main_comment)
                    st.write(side_comment)
                    # user_input_cosine.properties_closest_city()
                    user_input_cosine.info_other_similar_cities()
                

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
                            social_city_features = [ 'Nightlife Score', 'Beer Ranking',
                                                    'Festival Ranking', 'Tourism Score']
                            parameter_name = 'social'
                            try:
                                number = int(number)
                                if number == 0:
                                    st.warning('number must be greater than 0')
                                elif number <= 100 :
                                    user_input_feature2 = FeatureRecommendSimilar(social_city_features, number, parameter_name)
                                    user_input_feature2.calculate_top_cities_for_defined_feature()
                                    user_input_feature2.top_countries_based_on_selected_cities()
                                    with st.spinner("Analysing..."):
                                        time.sleep(2)
                                        user_input_feature2.decision_for_user_defined_city()
                                else:
                                    st.warning('number must be less than 100')
                            except ValueError:
                                st.warning('that was not a valid number. try again')
                        elif business:
                            business_city_features = ['Employment Score', 'Startup Score', 
                                                    'Transport Score', 'Immigration Tolerence' ]
                            parameter_name = 'business'
                            try:
                                number = int(number)
                                if number == 0:
                                    st.warning('number must be greater than 0')
                                elif number <= 100 :
                                    user_input_feature2 = FeatureRecommendSimilar(business_city_features , number, parameter_name)
                                    user_input_feature2.calculate_top_cities_for_defined_feature()
                                    user_input_feature2.top_countries_based_on_selected_cities()
                                    with st.spinner("Analysing..."):
                                        time.sleep(2)
                                        user_input_feature2.decision_for_user_defined_city()
                                else:
                                    st.warning('number must be less than 100')
                            except ValueError:
                                st.warning('that was not a valid number. try again')
                            pass
                        else:
                            femalefriendly_city_features = ['Access to Contraceptive Score', 
                                                            'Gender Equality Score','Personal Freedom and Choice']
                            parameter_name = 'female friendly'
                            try:
                                number = int(number)
                                if number == 0:
                                    st.warning('number must be greater than 0')
                                elif number <= 100 :
                                    user_input_feature2 = FeatureRecommendSimilar(femalefriendly_city_features , number, parameter_name)
                                    user_input_feature2.calculate_top_cities_for_defined_feature()
                                    user_input_feature2.top_countries_based_on_selected_cities()
                                    with st.spinner("Analysing..."):
                                        time.sleep(2)
                                        user_input_feature2.decision_for_user_defined_city()
                                else:
                                    st.warning('number must be less than 100')
                            except ValueError:
                                st.warning('that was not a valid number. try again')
                            
                            
                        
  
                
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
                                        user_input_feature2.decision_for_user_defined_city()
                                else:
                                    st.warning('number must be less than 100')
                            except ValueError:
                                st.warning('that was not a valid number. try again')

                        

    elif navigation == 'about':
        # st.components.v1.html(html, width=None, height=None, scrolling=False)
        html_code = """
        <div style="background-color:#91e6bf;padding:13px">
        <p><b>city_recommendation_app</b>  is web-app that can recommend cities for people to either <b>live or visitfor touristic purposes</b> . 
        The app was designed using a 2018 city ranking dataset generated by <b>NestPick</b>. The ranking was done primarilly by <b>millenials</b> . 
        The original data which I explored and used to generate the app can be found <a href="https://www.nestpick.com/millennial-city-ranking-2018/">here</a> </p>
        </div>
        <br>
        """
       
        '### Main info' 
        st.markdown(html_code, unsafe_allow_html=True)

        '###### There are two ways the app can recommened city to user:'
        '1. App looks for a city similar to one you like:'
        st.markdown(' - The app looks at a sets of parameters for the city you picked and calculates the most similar city based on cosine similarity algorithm (a colloaborative filtering method).' 
        ' - In simple terms, it looks at a certain sets of parameters such as Employment Score, Startup Score, Tourism Score, Housing Score,Access to Contraceptive Score, Gender Equality Score etc and calulate the city that is most similar to the city you picked.The parameters checked are 16 altogether' 
        '- It also suggests additional cities that are also quite similar under additional info'
        )
    
        '2. App can also look for a city based on a defined parameter:' 
        st.markdown(' - If all the 16 features used in option 1 are not important to you but only care about a few subsets, you can define your own parameters.' 
        'In this instance, the app will calculate the city with the highest score using your defined parameter.'
        'To show you an example, there are three predefined city feature but you can also define your own.'
        'You can select one or more features that define your city.'
        'For example, I defined a female friendly city with the following three features:'
        'Access to Contraceptive, Gender Equality, and Personal Freedom and Choice.')

        '- Here is a complete list of all the 16 parameters: Food Ranking, Transport Score, Health Rank,' 
        'Internet Speed Score, University Score, Access to Contraceptive Score, Gender Equality Score,'
        'Immigration Tolerence, Personal Freedom and Choice, LGBT friendly Score, Nightlife Score,' 
        'Beer Ranking,  Festival Ranking , Employment Score, Startup Score, Tourism Score, Housing Score'
            
        '### Deployment' 
        'This app was built with streamlit and deployed on Heroku through github.' 


        '### Design approach'
        st.markdown(
        'I could have easily designed the app using only funtions but for several reasons, I decided to generate classes:'
        'The first is that there are several functions and this will get messy as they grow.'
        'It also will assist potential person that clones the repo to figure out what function belongs to what'
        'Lastly, since I plan to extend the work in future using other colaborative methods,' 
        'it helps to organise by creating a different module for that method')
  
    

if __name__ == "__main__":
    app()
