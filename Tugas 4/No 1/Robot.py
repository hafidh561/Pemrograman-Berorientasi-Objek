from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self):
        self._nama: str = None
        self._pemilik: str = None
        self._tahun: int = None

    def setTahunPembuatan(self, tahun: int) -> None:
        self._tahun = tahun
        
    @abstractmethod
    def setNama(self, nama: str) -> None:
        self._nama = nama

    @abstractmethod
    def displayData(self) -> None:
        print("Nama:", self._nama)
        print("Pemilik:", self._pemilik)
        print("Tahun Pembuatan:", self._tahun)