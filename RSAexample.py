# Python program to demonstrate working of
# RSA Algorithm
     
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def crypto(mes, n, key):
    # mes = messaggio
    res = mes
    for jj in range(key-1):
        res = (mes*res)%n
    return res
    
    

if __name__ == '__main__':
    # Driver code
    p,q = 7,13
    n = p*q
    print("n = ", n)
    a = 5 # (a,n) = public key
    print("public key = ", "(", a, ",", n, ")")
    b = (p-1)*(q-1)
    print("b = ", b)
    g, x, y = gcdExtended(a, b)
    print("gcd(", a , "," , b, ") = ", g,x,y)
    print("private key = ", "(", x, ",", n, ")")

    mes = 3
    print("message = ", mes)
    mes_crypto = crypto(mes, n, a)
    print("crypted message = ", mes_crypto)
    #test mes2=mes
    mes2 = crypto(mes_crypto, n, x)
    print("de-crypted message = ", mes2)