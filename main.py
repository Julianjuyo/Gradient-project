
def PartialDerivativeX(x,y):

    return ((2*x*y)-(y**2))

def PartialDerivativeY(x,y):
    return ((x**2)-(2*x*y))

def calculateGradient(xCor,yCor):
    xCor = int(xCor)
    yCor = int(yCor)
    vector = [1,2]
    vector[0] = PartialDerivativeX(xCor,yCor)
    vector[1] = PartialDerivativeY(xCor, yCor)
    return vector

if __name__ == '__main__':

    print("The function that will be use is: f(x,y) = x²y - xy²")
    print("Write the coordinates of the plane.")
    print()

    while(True):
        print("Enter the numeric value for the x axis")
        xCor = "2" #input()
        if xCor.isnumeric():
            break
        print("Not valid entrance")

    while(True):
        print("Enter the numeric value for the y axis")
        yCor = "4" #input()
        if yCor.isnumeric():
            break
        print("Not valid entrance!!")

    print("the coordinates in x,y are: (" + xCor + " , " + yCor+")")

    ans = calculateGradient(xCor,yCor)
    print()
    print("The gradient at the coordinates (" + xCor + " , " + yCor+ ") is:")
    print(ans)