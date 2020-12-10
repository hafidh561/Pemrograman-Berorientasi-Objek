from Permainan import Permainan

class PermainanStrategy(Permainan):
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
        return hit * 5