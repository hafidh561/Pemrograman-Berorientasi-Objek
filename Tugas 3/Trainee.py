from Member import Member


class Trainee(Member):
    def __init__(self, nama: str, umur: int, lama_training: int):
        super().__init__(nama, umur)
        self.__lama_training = lama_training

    # Getter lama_training
    @property
    def lama_training(self):
        return self.__lama_training

    def display(self):
        super().display()
        print(f'Lama Training: {self.__lama_training}')
