# City_recommender_app

<img src="picture/city1.jpeg" alt="city" width="2000"/>

city_recommendation_app is web-app that can recommend cities for people to either live or visit for touristic purposes. 
I designed the app using a 2018 city ranking dataset generated by NestPick. The ranking was done primarilly by millenials. 
The original data which I explored and used to generate the app can be found [here](https://www.nestpick.com/millennial-city-ranking-2018/)


###### There are two ways the app can recommened city to user:

1. App looks for a city similar to one you like: 

- The app looks at a sets of parameters for the city you picked and calculates the most similar city based on cosine similarity algorithm (a colloaborative filtering method). 
In simple terms, it looks at a certain sets of parameters such as Employment Score, Startup Score, Tourism Score, Housing Score,Access to Contraceptive Score, 
Gender Equality Score etc and calulate the city that is most similar to the city you picked.The parameters checked are 16 altogether. 
It also suggests additional cities that are also quite similar under additional info
<br />

2. App can also look for a city based on a defined parameter: 

- If all the 16 features used in option 1 are not important to you but only care about a few subsets, you can define your own parameters. 
In this instance, the app will calculate the city with the highest score using your defined parameter.
To show you an example, there are three predefined city feature but you can also define your own. 
You can select one or more features that define your city.  
For example, I defined a female friendly city with the following three features:
 Access to Contraceptive, Gender Equality, and Personal Freedom and Choice.

- Here is a complete list of all the 16 parameters: Food Ranking, Transport Score, Health Rank, 
Internet Speed Score, University Score, Access to Contraceptive Score, Gender Equality Score, 
Immigration Tolerence, Personal Freedom and Choice, LGBT friendly Score, Nightlife Score, 
Beer Ranking,  Festival Ranking , Employment Score, Startup Score, Tourism Score, Housing Score
       

### Deployment 

This app was built with streamlit and deployed on Heroku. 
you can see it in action [here](https://ohteedee-city-recommender.herokuapp.com/) 

### Design approach

I could have easily designed the app using only funtions but for several reasons, I decided to generate classes:
The first is that there are several functions and this will get messy as they grow. 
It also will assist potential person that clones the repo to figure out what function belongs to what
Lastly, since I plan to extend the work in future using other colaborative methods, 
it helps to organise by creating a different module for that method.

### Info about files in the repo for potential people that may want to clone

- The data file contains the csv file containing the data used to generate the app

- The picture folder contains city picture used on the homepage of the app and in this README file

- The recommender folder contains .py files. The __init__.py is needed to package the directory, 
the cosine_recommender contains code for deined class used for recommending similar city based on cosine similarity, 
and feature_recommender contains code for deined class used for recommending based on your feartures or parameters

- The roughwork_jupyter folder contains the inital rough work used to exlore the data and generate funtions 

- The ''' app.py ''' file is the main file that powers the application and ''' util.py ''' contains code that are needed to load file and generate needed lists.

- The setup.sh and Procfile are needed for deployement on Heroku while the requirement.txt contains list of all the libraries used in the app. it is also needed for deployment.


### Replication of work
Feel free to clone the repo. 
If you have additional questions, you can send a message to me on [linkedin](https://www.linkedin.com/in/tosin-oyewale/)

### ----------------------------------------------------
app created by Tosin D. Oyewale (PhD) 
[Linkedin](https://www.linkedin.com/in/tosin-oyewale/) 




