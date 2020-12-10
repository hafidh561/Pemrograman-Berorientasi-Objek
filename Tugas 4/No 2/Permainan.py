from abc import ABC, abstractmethod

class Permainan(ABC):
    def __init__(self):
        self.__namaPemain: str = None
        self.__levelPemain: int = None

    def setNamaPemain(self, namaPemain: str) -> None:
        self.__namaPemain = namaPemain
        
    def setLevelPemain(self, levelPemain: int) -> None:
        if (levelPemain > 100):
            raise(ValueError("Level terlalu besar"))
        elif (levelPemain < 1):
            raise(ValueError("Level terlalu kecil"))
        self.__levelPemain = levelPemain
        
    def getNamaPemain(self) -> str:
        return self.__namaPemain
    
    def getLevelPemain(self) -> int:
        return self.__levelPemain
    
    def jalankan(self) -> None:
        hit = int(input("Masukkan jumlah hit: "))
        miss = int(input("Masukkan jumlah miss: "))
        print("Nama:", self.__namaPemain)
        print("Level:", end=" ")
        if (1 <= self.__levelPemain <= 20):
            print("Normal")
        elif (21 <= self.__levelPemain <= 80):
            print("Medium")
        elif (81 <= self.__levelPemain <= 100):
            print("Hard")
        print("Skor:", self.hitungSkor(hit, miss))

    @abstractmethod
    def hitungSkor(self, hit: int, miss: int) -> int:
        pass