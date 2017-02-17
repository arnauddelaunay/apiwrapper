# API WRAPPER

ApiWrapper wrap your ML model into an API.
Default routes are `predict` and `predict_proba`.

## Install

```
git clone https://github.com/arnauddelaunay/apiwrapper.git
cd apiwrapper
sudo pip install -r requirements.txt
```

## Usage

Once your model is loaded and fit, you can execute the api and pass the model as an argument

```
#!python
import apiwrapper
API = apiwrapper.Api(model=model)
API.run(port=5000, debug=True)
```

### Endpoints

 * **/** [GET] : info about the model
 * **/predict** [POST] : return the prediction of the model for the given input. FORMAT : {"data" : np.ndarray}
 * **/predict_proba** [POST] : return the prediction probabilities of the model for the given input. FORMAT : {"data" : np.ndarray}

### Complete exemple

Run `python main.py`

And test the API : 
```
curl -X POST -H "Content-Type: application/json" -d '{"data" : [
	[0.1, 0, 0.6, 1.2],
	[ 1.2,  1.3,  3.1, 1.8]
	]
}' "http://localhost:5000/predict"
```
gives the following results : `{"results": [0,2]}`.

## DOCKERIZE THE API

Use Docker to serve your API in background on the local network.

### Build
Go into the root of this repo

```
$ sudo docker build -t mymodel .
```

### Run

```
$ sudo docker run -d --name mycontainer -p 5000:5000 mymodel
```

### Test

Check your docker IP (here `172.17.0.1`):
```
$ ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:a8:32:08:90  
          inet adr:172.17.0.1  Bcast:0.0.0.0  Masque:255.255.0.0
          ... ... ...
          ... ... ...
```

You can now test the API : 
```
$ curl -X POST -H "Content-Type: application/json" -d '{"data" : [
	[0.1, 0, 0.6, 1.2],
	[ 1.2,  1.3,  3.1, 1.8]
	]
}' "http://172.17.0.1:5000/predict"
```
gives the following results : `{"results": [0,2]}`.





