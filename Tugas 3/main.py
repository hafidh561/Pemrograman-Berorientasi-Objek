from Member import Member
from Trainee import Trainee
from Tim import Tim


def main():

    members = [Member('Timbul', 23), Member('Jamalia', 21), Member('Ida', 20),
               Member('Uchita', 21), Member('Galih', 22), Member('Winda', 20)]

    newbies = [Trainee('Karen', 18, 1000), Trainee('Dewi', 19, 1200), Trainee('Gawati', 19, 900),
               Trainee('Eli', 18, 1250), Trainee('Dimaz', 19, 1150), Trainee('Kenari', 18, 1020)]

    team = Tim('Persitang', members)
    team.set_member(newbies)
    team.display_full_member()
    print()
    team.display_trainee()


if __name__ == '__main__':
    main()
