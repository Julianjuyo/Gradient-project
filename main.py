import numpy as np
import matplotlib.pyplot as plt


def PartialDerivativeX(x, y):
    return ((2 * x * y) - (y ** 2))


def PartialDerivativeY(x, y):
    return ((x ** 2) - (2 * x * y))


def calculateGradient(xCor, yCor):
    xCor = int(xCor)
    yCor = int(yCor)
    vector = [1, 2]
    vector[0] = PartialDerivativeX(xCor, yCor)
    vector[1] = PartialDerivativeY(xCor, yCor)
    return vector


def f(x, y):
    return ((x ** 2 * y) - (x * y ** 2))


if __name__ == '__main__':

    print("The function that will be use is: f(x,y) = x²y - xy²")
    print("Write the coordinates of the plane.")
    print()

    while (True):
        print("Enter the numeric value for the x axis")
        xCor = input()
        if xCor.isnumeric():
            break
        print("Not valid entrance")

    while (True):
        print("Enter the numeric value for the y axis")
        yCor = input()
        if yCor.isnumeric():
            break
        print("Not valid entrance!!")

    print("the coordinates in x,y are: (" + xCor + " , " + yCor + ")")

    ans = calculateGradient(xCor, yCor)
    print()
    print("The gradient at the coordinates (" + xCor + " , " + yCor + ") is:")
    print(ans)

    # x and y axis
    x = np.linspace(-1, 5, 10)
    y = np.linspace(-1, 5, 10)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_title('f(x,y) = x²y - xy²')
    plt.show()
