from Member import Member
from Trainee import Trainee


class Tim:
    def __init__(self, nama: str, members: list):
        self.__nama = nama
        self.__members = members

    def set_member(self, new_member: Member):
        self.__members.extend(new_member)

    def display_full_member(self):
        print('==========Member==========\n')
        for member in self.__members:
            if type(member) is Member:
                member.display()
                print()
        print('===========================')

    def display_trainee(self):
        print('==========Trainee==========\n')
        for member in self.__members:
            if type(member) is Trainee:
                member.display()
                print()
        print('===========================')

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, newName: str):
        self.__nama = newName
