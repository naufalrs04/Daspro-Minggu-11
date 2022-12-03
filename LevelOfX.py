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
            
def LevelOfX(P,X) :
    if not IsMember(P,X) :
        return 0
    else :
        if Akar(P)==X :
            return 0
        else :
            if IsBinerPB(P) :
                return 1 + LevelOfX(Left(P),X) + LevelOfX(Right(P),X)
            elif IsUnerLeftPB(P) :
                return 1 + LevelOfX(Left(P),X)
            elif IsUnerRightPB(P) :
                return 1 + LevelOfX(Right(P),X)

P = MakePb(2, MakePb(4,MakePb(7,None, None),MakePb(4,None,None)),MakePb(6,MakePb(2,None,None),MakePb(4,None,None)))

print (P)
print (LevelOfX(P,4))