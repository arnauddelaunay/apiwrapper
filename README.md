# API WRAPPER

ApiWrapper wrap your ML model into an API.
Default routes are `predict` and `predict_proba`.

## Install

```
git clone https://github.com/arnauddelaunay/apiwrapper.git
cd apiwrapper/
sudo pip install -r requirements.txt
```

## Usage

Once your model is loaded and fit, you can execute the api and pass the model as an argument

```
#!python
import apiwrapper
API = apiwrapper.Api(model=model)
API.run(port=3001, debug=True)
```

### Endpoints

 * **/** [GET] : info about the model
 * **/predict** [POST] : return the prediction of the model for the given input. FORMAT : {"data" : np.ndarray}
 * **/predict_proba** [POST] : return the prediction probabilities of the model for the given input. FORMAT : {"data" : np.ndarray}

### Complete exemple

A complete exemple using sklearn DecisionTreeClassifier on the iris dataset.

```
# Import our wrapper
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
print(model)

# Launch the API
API = apiwrapper.Api(model=model)
API.run(port=3001, debug=True)
```

You can now test the API : 
```
curl -X POST -H "Content-Type: application/json" -d '{"data" : [
	[0.1, 0, 0.6, 1.2],
	[ 1.2,  1.3,  3.1, 1.8]
	]
}' "http://localhost:3001/predict"
```
gives the following results : `{"results": [0,1]}`.





