from surprise import Dataset
from surprise.model_selection import KFold
from surprise.reader import Reader
from surprise import KNNBasic
from surprise import accuracy

reader = Reader(name="ml-100k")
data = Dataset.load_from_file("u.data", reader)

kf = KFold(n_splits=10)
k = 50


def calculate(sim_options):
    algo = KNNBasic(k=k, sim_options=sim_options)

    mae_results = []
    for trainset, testset in kf.split(data):
        algo.fit(trainset)
        predictions = algo.test(testset)
        mae_results.append(accuracy.mae(predictions))

    return mae_results


cosine = {'name': 'cosine', 'user_based': False}
pearson = {'name': 'pearson', 'user_based': True}

cosine_mae = calculate(cosine)
pearson_mae = calculate(pearson)


def average(lst):
    return sum(lst) / len(lst)


print(cosine_mae)
print("average cosine mae:" + str(average(cosine_mae)))
print(pearson_mae)
print("average pearson mae:" + str(average(pearson_mae)))

