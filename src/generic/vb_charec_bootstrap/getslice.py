import pickle, sys
arr = pickle.load(sys.stdin.buffer)
print(arr,arr[0:1],arr[0:2],type(arr))
