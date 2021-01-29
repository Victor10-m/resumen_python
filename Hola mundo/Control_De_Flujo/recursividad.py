def Recursion(i):
    if( i < 1):
        return(i)
    print(i)
    Recursion( i - 1)
Recursion(10)