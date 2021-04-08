DIMENSION = 200

def readFromFile(filename):

    file = open(filename, 'r')
    coordinates = [[] for j in range(DIMENSION)]
    
    while True: 
        line = file.readline().strip().split() 
        if not line: 
            break
        x = int(line[0])
        y = int(line[1])
        coordinates[x].append(y)
        
    file.close()
    return coordinates

def readVerification():
    coordinates = readFromFile('input.txt')
    for x in range(DIMENSION):
        if(len(coordinates[x]) > 0):
            print("X=" + str(x) , end =" Y:")
            for y in range(len(coordinates[x])):
                print(coordinates[x][y], end =" ")
            print("\n")
#readVerification()

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i

    return factorial

def main():
    coordinates = readFromFile('input3.txt')
    noRectangles = 0

    for i in range(DIMENSION):
        for j in range(i+1,DIMENSION):

            if (len(coordinates[i]) >= 2 and len(coordinates[j]) >= 2): 
                intersectionResult = intersection(coordinates[i], coordinates[j])
                lengthIntersection = len(intersectionResult)

                if (lengthIntersection >= 2 ):
                    #COMBINATION lengthIntersection TAKEN 2 => formula: C(n,k) = n! /(k!*(n-k)!)
                    noRectangles += factorial(lengthIntersection) / (2 * factorial(lengthIntersection-2))

    print(noRectangles)

main()





