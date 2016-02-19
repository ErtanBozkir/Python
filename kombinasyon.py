def kom(n,r):
    nr=(n-r)
    nrfaktoriyel=1
    while True:
        if (nr)==1:
            break

        else:
            nrfaktoriyel=nrfaktoriyel*(nr)
            (nr)=(nr)-1

    nfaktoriyel=1
    while True:
        if n==1:
            break

        else:
            nfaktoriyel=nfaktoriyel*n
            n=n-1

    rfaktoriyel=1
    while True:
        if r==1:
            break

        else:
            rfaktoriyel=rfaktoriyel*r
            r=r-1




    cvp=(nfaktoriyel/(rfaktoriyel*(nrfaktoriyel)))
    return(cvp)

n=int(input("C(n,r) n'i giriniz:"))
r=int(input("C(n,r) r'yi giriniz:"))

sonuc=kom(n,r)
print(int(sonuc))
