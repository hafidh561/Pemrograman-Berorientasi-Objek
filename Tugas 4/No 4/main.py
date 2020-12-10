from DoraMini import DoraMini

def main():
    robot = DoraMini()
    robot.setNama("Joko")
    robot.setPemilik("Budi")
    robot.setTahunPembuatan(1990)

    robot.displayData()
    print()
    robot.sayDora()
    print()
    robot.displayKantongAjaib()


if __name__ == '__main__':
    main()