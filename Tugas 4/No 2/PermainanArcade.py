from Permainan import Permainan

class PermainanArcade(Permainan):
    def __init__(self):
        super().__init__();
        
    def setNamaPemain(self, namaPemain: str) -> None:
        super().setNamaPemain(namaPemain)
        
    def setLevelPemain(self, levelPemain: int) -> None:
        super().setLevelPemain(levelPemain)
        
    def getNamaPemain(self) -> str:
        super().getNamaPemain()
    
    def getLevelPemain(self) -> int:
        super().getLevelPemain()
        
    def jalankan(self) -> None:
        super().jalankan()
        
    def hitungSkor(self, hit: int, miss: int) -> int:
        jumlah_hit = hit * 3
        jumlah_miss = miss * 1
        return jumlah_hit - jumlah_miss