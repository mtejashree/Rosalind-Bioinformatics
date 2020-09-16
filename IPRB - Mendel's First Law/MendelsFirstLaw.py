def MendelsFirstLaw(k,m,n):
    total = k+m+n
    p1 = k*(k-1)*2
    p2 = (m*(m-1)*3)/2
    p3 = k*m*4
    p4 = k*n*4
    p5 = m*n*2
    p6 = p1 + p2 + p3 + p4 + p5
    ans = p6/(2*total*(total-1))
    print(round(ans,5))
