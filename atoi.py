# your task is to complete this function
# function should return an integer
def atoi(string):
    # Code here
    try:
        num = int(string)
        return num
    except ValueError:
        return -1
    



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends
