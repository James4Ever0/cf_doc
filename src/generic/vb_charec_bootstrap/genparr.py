import numpy, pickle, sys
arr = numpy.array([1,2,3]).tolist()
pickle.dump(arr,sys.stdout.buffer)
# i mean can we slice normal array like this?
