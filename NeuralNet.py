import numpy as np
import math


class NeuralNet(object):
	#init the nn with constant weights and biases (to start with this network will always be untrained)
	# TODO in the future, it will be able to read weights and biases from a file 
	def __init__(self):
		self.layer1Weights = np.random.uniform(low=-1.0, high=1, size=(16, 784) )
		self.layer2Weights = np.random.uniform(low=-1.0, high=1, size=(16, 16) )
		self.layer3Weights = np.random.uniform(low=-1.0, high=1, size=(10, 16) )
		self.layer1Bias = np.zeros(16).reshape( (16,1 ) )
		self.layer2Bias = np.zeros(16).reshape( (16,1 ) )
		self.layer3Bias = np.zeros(10).reshape( (10,1 ) )
		#print(self.layer1Weights, "\n", self.layer2Weights, "\n", self.layer3Weights)
		
	#taken from delftstack.com/howto/python/sigmoid-function-python/
	def sigmoid(self, x):
		z = np.exp(-x)
		sig = 1 / (1 + z)
		return sig

	# interior func, for computes the activation of each layer 
	def computeStep(self, activationVector, layerWeights, bias):
		print(activationVector)
		nextLayer = layerWeights.dot(activationVector) + bias
		return self.sigmoid(nextLayer)

	def trainNetwork(self, trainingData):
		print("unimplemented Train Network")

	#main func, called by user to chose a digit.
	def choseDigit(self, imageVector):
		step = self.computeStep(imageVector, self.layer1Weights, self.layer1Bias)
		step = self.computeStep(step, self.layer2Weights, self.layer2Bias)
		step = self.computeStep(step, self.layer3Weights, self.layer3Bias)
		return step

