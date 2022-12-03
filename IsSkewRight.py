# NAMA  : NAUFAL RIZKI SAPUTRA
# NIM   : 24060122120011

from tree import *

def IsSkewRight(P) :
    if IsTreeEmpty(P) :
        False
    else :
        if IsUnerRightPB(P) == True and not IsOneElmtPB(P) :
            return IsSkewRight(Right(P))
        elif IsOneElmtPB(P) :
            True
        else :
            False

S = MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(5, None,None))))
P = MakePb(2, None, MakePb(4,None,MakePb(7,None, MakePb(5,MakePb(4,None,None),MakePb(6,None,None)))))

print(S)
print(P) 
print(IsSkewRight(S))
print(IsSkewRight(P))