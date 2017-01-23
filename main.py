import apiwrapper

# Sample Decision Tree Classifier
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


# load the iris datasets
dataset = datasets.load_iris()
# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)


app = apiwrapper.Api(model=model)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=5000)