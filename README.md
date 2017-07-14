# movielens_recommendation_system
Movie Recommendation system using python machine learning.
collaborative system _predicts what you like from the similar like of others
content based system _predicts what you like, based on what you previously liked in past
combination of both "Hybrid system"
#Dependencies required
pip install numpy
pip install scipy
pip install lightfm
lightfm is big library so only import sub modules and contains many other recommendation algorithms

#Data gathering
fetch datasets _ MOVIE LENS "csv file contains 1700 movies, 100,000 ratings out of 5 and 1000 users"
each user rated atleast 1 to 20 movies


create interaction matrix from csv file for only rating above 3.object
store this matrix from csv for creating recommendation model
data is stored as strings and we use strings to retrive data through dictionary
fectch_movielens will automatically seperates training and testing data set

ratio of train:testing 10:1

#storing model in variable

loss function weighted approximate rank pairwise
warp = check existing rating of user pairs and predicts ranking for each
it uses gradient descent to improve prediction
users past rating history(content based) + other users rating(collaborative)

train model use fit method
#Validation
print results
