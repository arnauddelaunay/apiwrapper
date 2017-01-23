# API WRAPPER

ApiWrapper wrap your ML model into an API.
Default routes are `predict` and `predict_proba`.

## Install

```
git clone https://github.com/arnauddelaunay/apiwrapper.git
cd apiwrapper/apiwrapper
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

Run `python main.py`

And test the API : 
```
curl -X POST -H "Content-Type: application/json" -d '{"data" : [
	[0.1, 0, 0.6, 1.2],
	[ 1.2,  1.3,  3.1, 1.8]
	]
}' "http://localhost:5000/predict"
```
gives the following results : `{"results": [0,1]}`.

## DOCKERIZE THE API

Use Docker to serve your API in background on the local network.

## Build
Go into the root of this repo

```
$ docker build -t mymodel .
```

## Run

```
$ docker run -d --name container2 -p 5000:5000 myimage
$ docker exec -d container2 python main.py
```

## Test

Check your docker IP (here `172.17.0.1`):
```
$ ifconfig
docker0   Link encap:Ethernet  HWaddr 02:42:a8:32:08:90  
          inet adr:_172.17.0.1_  Bcast:0.0.0.0  Masque:255.255.0.0
          adr inet6: fe80::42:a8ff:fe32:890/64 Scope:Lien
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Packets reçus:42133 erreurs:0 :0 overruns:0 frame:0
          TX packets:53797 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 lg file transmission:0 
          Octets reçus:2374630 (2.3 MB) Octets transmis:322282421 (322.2 MB)
```

You can now test the API : 
```
$ curl -X POST -H "Content-Type: application/json" -d '{"data" : [
	[0.1, 0, 0.6, 1.2],
	[ 1.2,  1.3,  3.1, 1.8]
	]
}' "http://172.0.17.1:5000/predict"
```
gives the following results : `{"results": [0,1]}`.





