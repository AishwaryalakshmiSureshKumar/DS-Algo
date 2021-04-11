hashtable = [[], ] * 10

def checkPrime(n):
    if n==1 or n==0:
        return 0
    for i in range(2, n//2):
        if n%i==0:
            return 0
    return 1

def getPrime(n):
    if n%2==0:
        n+=2
    while not checkPrime(n):
        n+=1
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key%capacity

def insertData(key, data):
    index = hashFunction(key)
    hashtable[index] =[key, data]

def removeData(key):
    index = hashFunction(key)
    hashtable[index] = 0


insertData(123, 'Aish')
insertData(234, 'Ish')

print(hashtable)

removeData(123)

print(hashtable)
