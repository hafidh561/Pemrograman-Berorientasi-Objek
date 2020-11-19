class Member:
    def __init__(self, nama: str, umur: int):
        self._nama = nama
        self._umur = umur

    # Setter umur
    def set_umur(self, newValue: int):
        self._var = newValue

    def display(self):
        print(f'Nama: {self._nama}')
        print(f'Umur: {self._umur}')
