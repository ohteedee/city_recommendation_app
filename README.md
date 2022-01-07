# city_recommendation_app

![image](picture/city1.jpeg)

###### This is an app that can recommend city for people, especially millennials. 
###### It takes your current city or city you have visited before that you liked a lot and suggest another city. 

###### There are two ways the app can recommened city to user:
1. look for a city similar to one you like: 
        The app looks at a sets of parameters for the city you picked and calculates the most similar city based on cosine similarity algorithm. 
        In simple terms, it looks at a certain sets of parameters such as Employment Score, Startup Score, Tourism Score, Housing Score,Access to Contraceptive Score, Gender Equality Score etc and calulate the city that is most similar to the city you picked
        The porameter checked are 16 altogether. It also suggests additional cities that are also quite similar under additional info
2. look for a city based on defined on a defined parameter
        If all the 16 features used in option 1 are not important to you but only care about a few subsets, you can define your own parameters
        To show you an example, there are three predefined city feature but you can also define your own 
        you can select one or more features that define your city.  for example, I defined a female friendly city as a city with Access to Contraceptive Score, Gender Equality Score and Personal Freedom and Choice

###### Here is a complete list of all the 16 parameters: Food Ranking, Transport Score, Health Rank, Internet Speed Score, University Score, Access to Contraceptive Score, Gender Equality Score, Immigration Tolerence, Personal Freedom and Choice,
######  LGBT friendly Score, Nightlife Score, Beer Ranking,  Festival Ranking , Employment Score, Startup Score, Tourism Score, Housing Score
       

### deployment 

you can see this app in action in the URL below


### deployment 
=======

This app was built with streamlit and deployed on Heroku. you can see it in action [here](https://ohteedee-city-recommender.herokuapp.com/) 

### 




