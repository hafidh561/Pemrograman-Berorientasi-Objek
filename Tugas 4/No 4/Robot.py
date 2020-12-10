from interface import Interface

class Robot(Interface):
    def setNama(self, nama: str) -> None:
        pass
    def setTahunPembuatan(self, tahun: int) -> None:
        pass
    def displayData(self) -> None:
        pass
