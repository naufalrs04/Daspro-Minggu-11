# Nama file : Type Pohon Biner
# Pembuat : Hasna Paramesti Ahmad
# Tanggal : 23 November 2020

# Definisi dan Spesifikasi Type
# Type Pohon Biner : <A:Elemen,L:Pohon Biner,R:Pohon Biner>
# {<A,L,R> adalah sebuah Pohon Biner, dengan A adalah Akar, L dan R adalah sub pohon kiri dan sub pohon kanan}
class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R
    def __repr__(self):  # Untuk merepresentasikan BinaryTree dalam bentuk string
        return "((%s, %s, %s))" % (repr(self.A), repr(self.L), repr(self.R))


# Fungsi Akar
# Akar : PohonBiner tidak kosong --> Elemen
# {Akar(P) adalah Akar dari P. Jika P adalah /L,A,R\ = Akar(P) adalah A}
def Akar(P):
    return P.A

# Fungsi Left
# Left : PohonBiner tidak kosong --> Elemen
# {Left(P) adalah sub pohon kiri dari P. Jika P adalah /L,A,R\ = Left(P) adalah L} 
def Left(P):
    return P.L

# Fungsi Right
# Right : PohonBiner tidak kosong --> Elemen
# {Right(P) adalah sub pohon kanan dari P. Jika P adalah /L,A,R\ = Right(P) adalah R} 
def Right(P):
    return P.R

# Fungsi MakePb
# MakePb : Pohon Biner --> Elemen
# {MakePb(A,L,R) membentuk sebuah Pohon Biner dari Akar, Left, dan Right}
def MakePb(A,L,R):
    return PohonBiner(A,L,R)

# Fungsi IsTreeEmpty
# IsTreeEmpty : PohonBiner --> boolean
# {IsTreeEmpty(P) true jika P adalah Pohon Biner kosong : (/\)}
def IsTreeEmpty(P):
    if P == None:
        return True
    else :
        return False

# Fungsi IsOneElmtPB
# IsOneElmtPB : Pohon Biner --> boolean
# {IsOneElmtPB(P) true jika P hanya mempunyai satu elemen yaitu /A}
def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else :
        return False

# Fungsi IsUnerLeftPB
# IsUnerLeftPB : Pohon Biner --> boolean
# {IsUnerLeftPB(P) true jika P mengandung sub pohon kiri}
def IsUnerLeftPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
        return True
    else :
        return False

# Fungsi IsUnerRightPB
# IsUnerRightPB : Pohon Biner --> boolean
# {IsUnerRightPB(P) true jika P mengandung sub pohon kanan}
def IsUnerRightPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Left(R)) and not IsTreeEmpty(Right(P))):
        return True
    else :
        False

# Fungsi IsExistLeftPB
# IsUnerExistPB : Pohon Biner --> boolean
# {IsUnerExistPB(P) true jika P mengandung sub pohon kiri}
def IsExistLeftPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P))):
        return True
    else :
        return False

# Fungsi IsExistRightPB
# IsUnerExistPB : Pohon Biner --> boolean
# {IsUnerExistPB(P) true jika P mengandung sub pohon kanan}
def IsExistRightPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P))):
        return True
    else :
        return False

# Fungsi IsBinerPB
# IsBinerPB : Pohon Biner --> boolean
# {IsBinerPB(P) true jika P mengandung sub pohon kiri dan sub pohon kanan}
def IsBinerPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(P)):
        return True
    else :
        return False

# Fungsi RepPrefixPB
# RepPrefixPB : Pohon Biner --> List of Element
# {RePrefixPB(P) memberikan representasi linier (dalam bentuk list), dengan urutan elemen list sesuai dengan urutan penulisan pohon secara prefix :
#   Basis : RepPrefiix(//\\) = []
#   Rekurens : RepPrefix (/L,A,R\) = [A] o RepPrefix(L) o RepPrefix(R) }
def RepPrefixPB(P):
    if IsOneElmtPB(P):
        return [Akar(P)]
    else :
        if IsBinerPB(P):
            return [Akar(P)] + RepPrefixPB(Left(P)) + RepPrefixPB(Right(P))
        elif IsUnerLeftPB(P):
            return [Akar(P)] + RepPrefixPB(Left(P))
        elif IsUnerRightPB(P):
            return [Akar(P)] + RepPrefixPB(Right(P))

# Fungsi NbElmt
# NbElmt : Pohon Biner --> integer >= 0
# {NbElmt(P) memberikan banyaknya elemen dari pohon P :
# Basis : NbElmt(//\\) = 0
# Rekurens : NbElmt(/L,A,R\) = NbElmt(L) + 1 + NbElmt(R)}
def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    else :
        return NbElmt(Left(P)) + 1 + NbElmt(Right(P))

# Fungsi NbDaunPB
# NbDaunPB : Pohon Biner --> integer >= 0
# {NbDaunPB(P) memberikan banyaknya daun dari pohon P :
# Basis-1 : NbDaun(//\\) = 0
# Rekurens :
#   NbDaun1(P)}
def NbDaunPB(P):
    if IsOneElmtPB(P):
        return 1
    elif IsBinerPB(P):
        return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
    elif IsUnerLeftPB(P):
        return NbDaunPB(Left(P))
    elif IsUnerRightPB(P):
        return NbDaunPB(Right(P))

P = MakePb(2,MakePb(3,MakePb(1,None,None),MakePb(5,None,None)),MakePb(3,MakePb(2,None,None),MakePb(4,None,None)))
#print(P)
#print(NbElmt(P))
#print(NbDaunPB(P))
print(IsUnerLeftPB(P))
print(IsExistLeftPB(P))