import NeuralNet
import DataParser

LFfile = "../datasets/training/train-labels-idx1-ubyte"
IFfile = "../datasets/training/train-images-idx3-ubyte" 
#step 1, parse files

parser = DataParser.DataParser()

data = parser.parse(IFfile, LFfile) 


#step 2, NN
net = NeuralNet.NeuralNet()

outputVector = net.choseDigit(data[1][1])
#print(data[1][1])
print(outputVector)
#step 4 profit 
