#!flask/bin/python
from flask import Flask, request, jsonify
import json

import numpy as np

from exceptions import WrapperError

nomodelmessage = "No model loaded yet."\
    "Run api.load_model(model) before launching the api"


class Api(object):
	'''
    Class to wrap a ML model into a callable API
    model must have predict and predict_proba function
    Bonus : load an helper function with the model for
    the API to give info about the goal of the model
    '''
	def __init__(self, model=None, helper=None):
		self.app = Flask(__name__)
		self.model = model
		self.reload_routes()
		self.helper = helper
		self.register_errors()

	def register_errors(self):
		@self.app.errorhandler(WrapperError)
		def handle_invalid_usage(error):
			response = jsonify(error.to_dict())
			response.status_code = error.status_code
			return response

	def load_model(self, model, helper=None):
		self.model = model
		if helper:
			self.helper = helper
		self.reload_routes()

	def reload_routes(self):
		@self.app.route('/', methods=['GET'])
		def index():
			if self.helper:
				return self.helper
			else:
				message = "APIwrapper for ML models.\n"
				if self.model:
					return message + "Model loaded and ready."
				else:
					raise WrapperError(nomodelmessage)

		@self.app.route('/predict', methods=['POST'])
		def predict():
			if not self.model:
				raise WrapperError(nomodelmessage)
			else:
				if 'data' not in request.json:
					raise WrapperError('Wrong Input Format', status_code=401)
				X_test = np.array(request.json['data'])
				shape = X_test.shape
				if len(shape) < 2:
					X_test = X_test.reshape(1, -1)
				result = self.model.predict(X_test)
				return jsonify(results=result.tolist())

		@self.app.route('/predict_proba', methods=['POST'])
		def predict_proba():
			if not self.model:
				raise WrapperError(nomodelmessage)
			else:
				if 'data' not in request.json:
					raise WrapperError('Wrong Input Format', status_code=401)
				X_test = np.array(request.json['data'])
				shape = X_test.shape
				if len(shape) < 2:
					X_test = X_test.reshape(1, -1)
				result = self.model.predict_proba(X_test)
				print result
				return jsonify(results=result.tolist())

	def run(self, **kwargs):
		self.app.run(**kwargs)
