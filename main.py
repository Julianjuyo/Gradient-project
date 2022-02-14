# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def calculateGradient(name):
    # Use a breakpoint in the code line below to debug your script.


    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print()
    print("The function that will be use is: f(x,y) = x²y - xy²")
    print()
    print("Write the coordinates of the plane.")
    print()

    while(True):
        print("Enter the numeric value for the x axis")
        x = input()
        if x.isnumeric():
            break
        print("Not valid entrance")

    while(True):
        print("Enter the numeric value for the y axis")
        y = input()
        if y.isnumeric():
            break
        print("Not valid entrance!!")

    #function = ((x^2*y) - (x*y^2))


    print("the coordinates in x,y are: "+ x +" , "+ y)


    #calculateGradient(input)

