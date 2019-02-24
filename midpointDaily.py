""" File to test the midpoint rule for integration 
M410 
Thad Haines
02/23/19
"""
import math
#import matplotlib.pyplot as plt # for plotting

def f(x):
    """Function that is to be integrated"""
    return (2*math.sin(10*x+1)+1)

def fpp(x):
    """Double prime of f (used for error calculation)"""
    return (-200*math.sin(10*x+1))

def F(x):
    """Antiderivative (i.e. integrated function) of f"""
    return (x - (1/5)*math.cos(10*x+1) )

def midpoint(f, x0, h):
    """Midpoint integration
    f = function handle
    x0 = left hand point of stencil
    h = step size
    """
    return 2*h*f(x0+h);

def midpointError(fpp, h, xi):
    """Return calculated error"""
    return (h**3*fpp(xi))

def checkInput(userInput):
    """Check input to see if exit loop desired"""
    if userInput == 'exit':
        return 0
    return 1

if __name__ == "__main__":
    print("Midpoint rule")
    print("f = 2*math.sin(10*x+1)+1")
    print("F = x - (1/5)*math.cos(10*x+1)")
    print("Enter 'exit' to exit (no quotes)")
    flag = 1
    while flag:
        # get and check user input
        x0 = input("x0 = ")
        flag = checkInput(x0)
        if not flag:
            continue

        h = input("h = ")
        flag = checkInput(h)
        if not flag:
            continue

        # cast input as floats
        x0 = float(x0)
        h = float(h)

        # set and calculate bound of integration
        a = x0
        b = 2*h+x0

        mpApprox = midpoint(f,x0,h)

        # find xi and predicted error bound
        if abs(fpp(a)) > abs(fpp(b)):
            xi = a
        else:
            xi = b

        mpErrBound = abs(midpointError(fpp, h, xi))

        # Calculate exact integral
        exactInt = F(b) - F(a)

        # Calculate actual midpoint error
        mpErr = abs(mpApprox - exactInt)

        print("***")
        print("a\tb\th\tMPaprx\terrBnd\tErr\tExactIntegral")
        print("%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t" %
              (a,b,h,mpApprox,mpErrBound,mpErr,exactInt))
        print("***")
    