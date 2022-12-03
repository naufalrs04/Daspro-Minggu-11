# NAMA  : NAUFAL RIZKI SAPUTRA
# NIM   : 24060122120011

from tree import *

def IsMember(P,X) :
    if IsTreeEmpty(P) :
        False
    else :
        if Akar(P)==X :
            True
        else :
            return IsMember(Left(P),X) or IsMember(Right(P),X)

S = MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(7, None,None))))
P = MakePb(2,MakePb(3,MakePb(1,None,None),MakePb(5,None,None)),MakePb(3,MakePb(2,None,None),MakePb(4,None,None)))

print(S)
print(P)
print(IsMember(S,5))
print(IsMember(P,7))
