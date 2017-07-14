#collaborative system _predicts what you like from the similar like of others
#content based system _predicts what you like, based on what you previously liked in past
#combination of both "Hybrid system"
#Dependencies required
#pip install numpy
#pip install scipy
#pip install lightfm
#lightfm is big library so only import sub modules and contains many other recommendation algorithms
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch datasets _ MOVIE LENS "csv file contains 1700 movies, 100,000 ratings out of 5 and 1000 users"
#each user rated atleast 1 to 20 movies
data = fectch_movielens(min_rating = 3.0)

#above method will create interaction matrix from csv file for only rating above 3.object
#store this matrix from csv for creating recommendation model
#data is stored as strings and we use strings to retrive data through dictionary
#fectch_movielens will automatically seperates training and testing data set
print(repr(data['train']))
print(repr(data['test']))
#above will be in ratio of train:testing 10:1

#storing model in variable
model = LightFM(loss = 'warp')
#loss function weighted approximate rank pairwise
#warp = check existing rating of user pairs and predicts ranking for each
#it uses gradient descent to improve prediction
#users past rating history(content based) + other users rating(collaborative)

#to train model use fit method
model.fit(data['train'], epochs = 40, num_threads = 3)


def recommendation_system(model,data,user_ids):
	n_users, n_items = data['train'].shape
	
	for user_id in user_ids:
		#movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
		#movies our model predict
		scores = model.predict(user_id, np.arange(n_items))
		#rank them in order of most liked to least
		top_items = data['item_labels'][np.argsort(-scores)]
		
		#print results
		print("User %s" % user_id)
		print("		Known Positives")
		
		for x in known_positives[:3]:
			print("		%s" % x)
		print("Recommended : " )
		for x in top_items[:3]:
			print("		%s" % x)
		
		
recommendation_system(model, data, [3,25,480])