

def comparator(a,b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba)>int(ab)) - (int(ba)<int(ab)))

def myCompare(mycomp):

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycomp(self.obj, other.obj)<0
        def __gt__(self, other):
            return mycomp(self.obj, other.obj)>0
        def __eq__(self, other):
            return mycomp(self.obj, other.obj)==0
        def __le__(self, other):
            return mycomp(self.obj, other.obj)<=0
        def __ge__(self, other):
            return mycomp(self.obj, other.obj)>=0
        def __ne__(self, other):
            return mycomp(self.obj, other.obj)!=0
    return K


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=[int(x) for x in input().split()]
    sorted_array = sorted(arr, key=myCompare(comparator))
    number="".join([str(i) for i in sorted_array])
    print(number)
