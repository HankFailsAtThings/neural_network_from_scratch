
#
#	Objects of this class parses files provided of the format described here http://yann.lecun.com/exdb/mnist/ 
#		into a tuple including 
#			1, vectors 1x784 representing the grey scale pixels of each image
#			2, the handwritten integer 
#
import struct


class DataParser(object): 

	def __init__(self):
		self.outputList = []

	def parse(self, imageFile, labelFile):
		#open files
		#check magic byte
		self.IFHandle = open(imageFile, 'rb')
		self.LFHandle = open(labelFile, 'rb')
		IFHeader = struct.unpack('>II',self.IFHandle.read(8))
		LFHeader = struct.unpack('>II',self.LFHandle.read(8))
		imageMagicNumber = IFHeader[0]
		labelMagicNumber = LFHeader[0]
		imageFileSz = IFHeader[1]
		labelFileSz = LFHeader[1]
		if imageMagicNumber != 2051:
			print("invalid file type, DataParser did not recognize %s's magic number" % imageFile)
		if labelMagicNumber != 2049:
			print("invalid file type, DataParser did not recognize %s's magic number" % labelFile)
		#check if the number of images == the number of labels 
		if imageFileSz != labelFileSz:
			print("file size mismatch: %s and %s do not contain the same number of elements".format(imageFile, labelFile))
		# 2x 32 bit ints representing row/col (should be 28x28)
		#28*28 pixels (each pixel is an unsigned byte) 
		raw_rc = struct.unpack('>II', self.IFHandle.read(8))
		rows = raw_rc[0]
		cols = raw_rc[1] 
		if rows != 28 or cols != 28:
			print("something wird, row/col not 28, its %d %d instead" % (rows,cols))

		for item in range(10):  # 10 for inital tests
			self.outputList.append((self.parseLabel(self.LFHandle), self.parseImage(self.IFHandle)))
		return self.outputList
		#pass to relevent parser 	

	def parseLabel(self, file):
		#each label is a single byte, can make this faster by chunking data, don't care ATM 
		return struct.unpack('>B', self.LFHandle.read(1))[0]

	def parseImage(self, file):
		image =  self.IFHandle.read(784)
		bitmapImage = struct.unpack(">784B", image) 
		return bitmapImage
			
		
	

