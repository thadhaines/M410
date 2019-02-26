""" File to test the trapezodial rule for integration 
M410 
Thad Haines
02/25/19
Using ipy -> Make sure to explicitly use decimals for proper casting...
"""
import math
#import matplotlib.pyplot as plt # for plotting

def f(x):
    """Function that is to be integrated"""
    return (2.0*math.sin(10.0*x+1.0)+1.0)

def fpp(x):
    """Double prime of f (used for error calculation)"""
    return (-200.0*math.sin(10.0*x+1.0))

def F(x):
    """Antiderivative (i.e. integrated function) of f"""
    soln = x - (1.0/5.0)*math.cos(10.0*x+1.0) 
    return soln

def midpoint(f, x0, h):
    """Midpoint integration
    f = function handle
    x0 = left hand point of stencil
    h = step size
    """
    return 2.0*h*f(x0+h);

def midpointError(fpp, h, xi):
    """Return calculated error"""
    return (h**3*fpp(xi))

def trapezoidal(f, x0, h):
    """Calculate area via trapezoidal rule"""
    return (h/2.0 * (f(x0)+f(x0+h)))

def tzError(fpp, h, xi):
    """Return calculated error estimate"""
    return (h**3*fpp(xi))

def checkInput(userInput):
    """Check input to see if exit loop desired"""
    if userInput == 'exit':
        return 0
    return 1

if __name__ == "__main__":
    print("Trapezoidal rule")
    print("f = 2*math.sin(10*x+1)+1")
    print("F = x - (1/5)*math.cos(10*x+1)")
    print("Enter 'exit' to exit (no quotes)")
    flag = 1
    while flag:
        # get and check user input
        x0 = raw_input("x0 = ")
        flag = checkInput(x0)
        if not flag:
            continue

        h = raw_input("h = ")
        flag = checkInput(h)
        if not flag:
            continue

        # cast input as floats
        x0 = float(x0)
        h = float(h)

        # set and calculate bound of integration
        a = x0
        b = h+x0

        tzApprox = trapezoidal(f,x0,h)

        # find xi and predicted error bound
        # check for largest bound
        if abs(fpp(a)) > abs(fpp(b)):
            xi = a
        else:
            xi = b
        # check center point also
        if abs(fpp(x0+0.5*h)) > abs(fpp(xi)):
            xi = x0

        tzErrBound = abs(tzError(fpp, h, xi))

        # Calculate exact integral
        exactInt = F(b) - F(a)

        # Calculate actual midpoint error
        tzErr = abs(tzApprox - exactInt)

        print("***")
        print("a\tb\th\tTZaprx\terrBnd\tErr\tExactIntegral")
        print("%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t" %
              (a,b,h,tzApprox,tzErrBound,tzErr,exactInt))
        print("***")
    