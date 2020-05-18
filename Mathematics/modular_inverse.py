'''
1) Naive Method, O(m)
2) Extended Euler’s GCD algorithm, O(Log m) [Works when a and m are coprime]
3) Fermat’s Little theorem, O(Log m) [Works when ‘m’ is prime]
 a x ≡ 1 (mod m) 
'''

# A naive method to find modulor  
# multiplicative inverse of 'a'  
# under modulo 'm' 
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

'''
ax + by = gcd(a, b) 
To find multiplicative inverse of ‘a’ under ‘m’, we put b = m in above formula. Since we know that a and m are relatively prime, we can put value of gcd as 1.
 ax + my = 1 
If we take modulo m on both sides, we get
 ax + my ≡ 1 (mod m)
We can remove the second term on left side as ‘my (mod m)’ would always be 0 for an integer y.
 ax  ≡ 1 (mod m) 
 '''
 # Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 
  
# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
  
  
  '''
  a^m-1 ≡ 1 (mod m)  
If we multiply both sides with a-1, we get
 a^-1 ≡ a^ m-2 (mod m)
 '''
# Function to find modular 
# inverse of a under modulo m 
# Assumption: m is prime 
def modInverse(a, m) : 
      
    g = gcd(a, m) 
      
    if (g != 1) : 
        print("Inverse doesn't exist") 
          
    else : 
          
        # If a and m are relatively prime, 
        # then modulo inverse is a^(m-2) mode m 
        print("Modular multiplicative inverse is ", 
                                    power(a, m - 2, m)) 
      
# To compute x^y under modulo m 
def power(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
  
# Function to return gcd of a and b 
def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a) 
      
  



'''
Applications:
Computation of the modular multiplicative inverse is an essential step in RSA public-key encryption method.
'''
