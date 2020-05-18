from math import floor

def quadraticRoots(a,b,c):
    
    x=b**2- 4*a*c
    
    if x<0:
        print( "Imaginary")
    else:
        print( floor((-b+(x)**0.5)/a/2),floor((-b-(x)**0.5)/a/2))
