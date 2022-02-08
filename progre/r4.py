n =1
def rec(n):
    if n <=8:
        rec(n+1)
    def pattern(m):
        print(m,end=" ")
        if m<6:
            pattern(m)
    pattern(m)
    return(n)
(rec(n))