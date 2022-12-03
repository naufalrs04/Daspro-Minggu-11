# NAMA  : NAUFAL RIZKI SAPUTRA
# NIM   : 24060122120011

from tree import *

def IsSkewLeft(P) :
    if IsTreeEmpty(P) :
        False
    else :
        if IsUnerLeftPB(P) == True and not IsOneElmtPB(P) :
            return IsSkewLeft(Left(P))
        elif IsOneElmtPB(P) :
            True
        else :
            False

S = MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(5, None,None))))
P = MakePb(2, None, MakePb(3,None,MakePb(1,None, MakePb(7,MakePb(4,None,None),MakePb(2,None,None)))))

print(S)
print(P) 
print(IsSkewLeft(S))
print(IsSkewLeft(P))