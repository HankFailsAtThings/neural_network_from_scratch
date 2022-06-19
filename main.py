import DataParser


LFfile = "../datasets/training/train-labels-idx1-ubyte"
IFfile = "../datasets/training/train-images-idx3-ubyte" 
#step 1, parse files

parser = DataParser.DataParser()

parser.parse(IFfile, LFfile) 


#step 3 , uhh 

#step 4 profit 
