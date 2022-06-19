import DataParser
import numpy as np 
#some test code
#represent the images parsed by dataparser.py 




LFfile = "../datasets/training/train-labels-idx1-ubyte"
IFfile = "../datasets/training/train-images-idx3-ubyte"
#step 1, parse files

parser = DataParser.DataParser()

rawimages = parser.parse(IFfile, LFfile)

def zeroOrOne(x):
	if x == 0:
		return 0
	else: 
		return 1

for item in rawimages:
	number = item[0]
	imageArray = np.array([zeroOrOne(i) for i in item[1]])
	shape = (28,28)
	image = imageArray.reshape( shape )
	print(number)
	print(image)


	 



