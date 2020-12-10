from Permainan import Permainan
from PermainanArcade import PermainanArcade
from PermainanStrategy import PermainanStrategy

def main():
    print("Permainan Arcade")
    permainan1 = PermainanArcade()
    permainan1.setNamaPemain("Budi")
    permainan1.setLevelPemain(50)
    permainan1.jalankan()
    
    print()
    
    print("Permainan Strategy")
    permainan2 = PermainanStrategy()
    permainan2.setNamaPemain("Joko")
    permainan2.setLevelPemain(20)
    permainan2.jalankan()

if __name__ == "__main__":
    main()