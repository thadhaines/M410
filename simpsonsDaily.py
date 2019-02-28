""" File to compare trapezoidal to simpsons 1/3 and 3/8 integration rule
M410 
Thad Haines
02/28/19
If using ipy -> Make sure to explicitly use decimals for proper casting...
"""
import math

def f(x):
    """Function that is to be integrated"""
    return (2.0*math.sin(10.0*x+1.0)+1.0)

def fpp(x):
    """Double prime of f (used for error calculation)"""
    return (-200.0*math.sin(10.0*x+1.0))

def fppp(x):
    """Third derivative (for fun)"""
    return (-2000.00*math.cos(10.0.x+1))

def fpppp(x):
    """The fourth derivative of f (used for error approximation)"""
    return (20000.0*math.sin(10.0*x+1.0))

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

def tzError(fpp, h, xiTz):
    """Return calculated error estimate"""
    return (h**3*fpp(xiTz))

def simp13(f, x0, h13):
    """Calculate integral using simpsons 1/3 rule"""
    return ((h13/3.0)*(f(x0) + 4.0*f(x0+h13) + f(x0+2.0*h13)))

def simp38(f, x0, h38):
    """Calculate integral using simpsons 3/8 rule"""
    return ((3.0*h38/8.0)
            *(f(x0) + 3.0*f(x0+h38) + 3.0*f(x0+2.0*h38) + f(x0 + 3.0*h38)))

def simpError(fppp, h, xiSimp):
    """Calculate simpson error approx (same for either 1/3 ro 3/8)"""
    return (h**5*fppp(xiSimp))

def checkInput(userInput):
    """Check input to see if exit loop desired"""
    if userInput == 'exit':
        return 0
    return 1

if __name__ == "__main__":
    print("Trapezoidal / Simpson's rule Comparison")
    print("f = 2*math.sin(10*x+1)+1")
    print("F = x - (1/5)*math.cos(10*x+1)")
    print("To exit: Type 'exit' (no quotes) as an input.")
    flag = 1
    while flag:
        # get and check user input
        x0 = raw_input("x0 = ")
        flag = checkInput(x0)
        if not flag:
            continue

        b = raw_input("b = ")
        flag = checkInput(b)
        if not flag:
            continue

        # cast input as floats
        x0 = float(x0)
        b = float(b)

        # set and calculate bound of integration
        a = x0
        hTz = b-a
        h13 = (b-a)/2.0
        h38 = (b-a)/3.0

        # calculate approximates
        tzApprox = trapezoidal(f,x0,hTz)
        s13Approx = simp13(f, x0, h13)
        s38Approx = simp13(f, x0, h38)

        # find xiTz and predicted error bound - Trapezoidal Error
        # check for largest bound
        if abs(fpp(a)) > abs(fpp(b)):
            xiTz = a
        else:
            xiTz = b
        # check center point also
        if abs(fpp(x0+0.5*hTz)) > abs(fpp(xiTz)):
            xiTz = x0

        tzErrBound = abs(tzError(fpp, hTz, xiTz))

        # find xiSimp and predicted error bound - Simpson error
        # check for largest bound
        if abs(fpppp(a)) > abs(fpppp(b)):
            xiSimp = a
        else:
            xiSimp = b
        # check center point also
        if abs(fpppp((a+b/2.0))) > abs(fpppp(xiSimp)):
            xiSimp = (a+b/2.0)

        s13ErrBound = abs(simpError(fpppp, h13, xiSimp))
        s38ErrBound = abs(simpError(fpppp, h38, xiSimp))

        # Calculate exact integral
        exactInt = F(b) - F(a)

        # Calculate actual error
        tzErr = abs(tzApprox - exactInt)
        s13Err = abs(s13Approx - exactInt)
        s38Err = abs(s38Approx - exactInt)

        print("***")
        print("type \ta \tb \th \tApprx \tErrEst \tErr \tExactInt")
        print("TZ \t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g" %
              (a,b,hTz,tzApprox,tzErrBound,tzErr,exactInt))
        print("S13 \t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g" %
              (a,b,h13,s13Approx,s13ErrBound,s13Err,exactInt))
        print("S38 \t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g\t%.3g" %
              (a,b,h38,s38Approx,s38ErrBound,s38Err,exactInt))
        print("***")
    