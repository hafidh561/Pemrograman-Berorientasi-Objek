from Robot import Robot


class DoraMini(Robot):
    def __init__(self):
        super().__init__()

    def sayDora(self) -> None:
        print("Halo, Saya Dora Mini")

    def setTahunPembuatan(self, tahun: int) -> None:
        self._tahun = tahun
        
    def setNama(self, nama: str) -> None:
        self._nama = nama
        
    def displayData(self) -> None:
        print("Nama:", self._nama)
        print("Pemilik:", self._pemilik)
        print("Tahun Pembuatan:", self._tahun)