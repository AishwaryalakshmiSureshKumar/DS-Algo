import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    print(len(numpy.array(arr)))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
