from interface import implements
from Robot import Robot
from Doraemon import Doraemon

class DoraMini(implements(Robot, Doraemon)):
    def __init__(self):
        self.__nama: str
        self.__pemilik: str
        self.__tahun: int

    def getPemilik(self) -> str:
        return self.__pemilik

    def setPemilik(self, pemilik: str) -> str:
        self.__pemilik = pemilik

    # Instance interface Robot
    def setNama(self, nama: str) -> None:
        self.__nama = nama
    def setTahunPembuatan(self, tahun: int) -> None:
        self.__tahun = tahun
    def displayData(self) -> None:
        print("Nama:", self.__nama)
        print("Pemilik:", self.__pemilik)
        print("Tahun:", self.__tahun)
    
    # Instance interface Doraemon
    def sayDora(self) -> None:
        print("Halo, Saya Dora Mini")
    def displayKantongAjaib(self) -> None:
        print("Saya juga seperti Doraemon yang memiliki Kantung ajaib")