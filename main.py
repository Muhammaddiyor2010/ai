class Mushuk():
    def __init__(self, rang, laqab, vazn, dum, yosh):
        self.rang = rang
        self.laqab = laqab
        self.vazn = vazn
        self.dum = dum
        self.yosh = yosh

    def miyovlash(self):
        return f"{self.laqab} miyovlaydi."
    
Oqmushuk = Mushuk("oq","Qoravoy",2,True,5)

print(f"{Oqmushuk.laqab} - {Oqmushuk.rang} rangli mushuk, vazni {Oqmushuk.vazn} kg,  {Oqmushuk.yosh} yoshda.")

if Oqmushuk:
    Oqmushuk.dum = True
    print(f"{Oqmushuk.laqab} ni dumi bor")
else:
    print(f"{Oqmushuk.laqab} ni dumi yo'q")