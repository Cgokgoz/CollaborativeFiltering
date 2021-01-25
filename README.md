# CollaborativeFiltering
Collaborative filtering is a technique that can filter out items that a user might like on the basis of
reactions by similar users. There are many ways to decide which users are similar and combine their
choices to create a list of recommendations.
The Movielens 100k dataset is a stable benchmark dataset with 100,000 ratings given by 943 users
for 1682 movies, with each user having rated at least 20 movies.

• u.item: the list of movies
• u.data: the list of ratings given by users

In this project, ultimate goal is to predict the rating given to
a movie by a specific (target) user. Python library was used
to achieve the project purpose ;Surprise is a Python scikit
for building and analyzing recommender systems that deal
with explicit rating data. Implemented the dataset module to
the code to use the file containing the data. The data was
made available with the load_from_file method.

In K-Folds Cross Validation, we splitting our data into k different subsets. We use k-1 subsets to
train our data and leave the last subset as test data. The average error value obtained as a result of k
experiments indicates the validity of our model and allows us to avoid overfitting. Splitting the
dataset into train and test sets, I will follow 10-fold cross validation strategy. Model_selection
package and KFold module were implemented.

User based collaborative filtering approach relies on the idea that users who have similar rating
behaviors, share the same tastes, and will likely exhibit similar rating behaviors going forward. User
based collaborative filtering is an algorithmic framework where the neighboring users are identified
based on the similarity with the active user, and then scoring of the items is done based on
neighbor’s ratings followed by a recommendation of an item based item’s scores by the
recommendation system. The similarity between users ( also known as the distance between users)
is a mathematical method to quantify how different or similar users are to each other. Similarity,
sim xγ between the users x and y who have both rated the same items is calculated first. To calculate
this similarity different metrics are used. We will be using correlation-based similarity metrics to
compute the similarity between user x and user y, sim xγ using pearson correlation.

Item-based collaborative filtering approach for recommender systems based on the similarity
between items calculated using people's ratings of those items.[2]Item-based models use rating
distributions per item, not per user. Similarities between pair of items are computed using cosine
similarity metric.

KNN classifies the new data points based on the similarity measure of the earlier stored data points.
K in KNN represents the number of the nearest neighbors we used to classify new data points. To
get the best results, it is necessary to find the optimal k value.For this, mean absolute error values
should be checked. Mean absolute error (MAE) is a measure of error between paired observations
expressing the same phenomenon. The lower the MAE value, the higher the accuracy.

The algorithm on the left is used to find the mean absolute
error values using knn. When the results were examined
(The lower the MAE value, the higher the accuracy.), it was
seen that the most optimal k value was 50 for both
approaches.
Almost every tech company uses recommendation systems
to provide its users a better experience. There are several
types of methods to build a recommendation system. In this
project, we gave 10 fold value and separated it as train and
test. We analyzed the data in User-based CF with Pearson
correlation, Item-based CF with cosine similarity in two
approaches. We classified the data using knn and
investigated the Mean Absolute Error values for the most
optimal k value and accuracy.

The MovieLens 100K Dataset is publicly available. 
Please visit https://grouplens.org/datasets/movielens/100k/todownload the dataset.

References
[1]:https://realpython.com/build-recommendation-engine-collaborative-filtering/
[2]:https://en.wikipedia.org/wiki/Item-item_collaborative_filtering
