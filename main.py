"""
Vykreslenie 6 tvaroch diamantu. Tento program je podobny pre vykreslovanie popuarnej piramidy ale jedna sa o vykreslovanie diamantoveho tvaru do terminalu

 /\
/  \
\  /
 \/
 /\
//\\
\\//
 \/
  /\
 /  \
/    \
\    /
 \  /
  \/
  /\
 //\\
///\\\
\\\///
 \\//
  \/
   /\
  /  \
 /    \
/      \
\      /
 \    /
  \  /
   \/
   /\
  //\\
 ///\\\
////\\\\
\\\\////
 \\\///
  \\//
   \/
"""


def main():

#vykreslenie jednoho z 6 tvarou diamantu
#tato velkost sa da upravit pri zmene maximalneho rozsahu v: range(0, x)
#pricom ked nastavime x ako lubovolne kladne cele cislo tak vykresi teda maximalne tuto velkost v terminaly
#vykresluje od 1 po max hodnotu obsiahnutu v range
    for diamantSize in range(0, 6):
        displayOtlineDiamond(diamantSize)
        print()
        displayFilledDiamond(diamantSize)
        print()

def displayOtlineDiamond(size):
    #vykreslenie vrchnej polovice
    for i in range (size):
        print(" " * (size - i - 1), end = "") #lava medzera
        print("/", end = "") #lava strana
        print(" " * (i * 2), end = "") #vnutrajsok diamantu
        print("\\") #prava strana diamantu

    #vykreslenie spodnej strany diamantu
    for i in range(size):
        print(" " * i, end = "") #lava medzera
        print("\\", end = "") #vykresmenie avej strany diamantu
        print(" " * ((size - i -1) * 2), end = "") #vnutrajsok diamantu
        print("/") #dokoncenie pravej strany diamantu

def displayFilledDiamond(size):
    #vykreslenie vrchnej casti diamantu
    for i in range(size):
        print(" " * (size - i - 1), end = "") #vykreslenie medzery na lavej strane
        print("/" * (i + 1), end = "") #lava strana diamantu
        print("\\" * (i + 1)) #prava strana diamantu

    #vykreslenie spodnej casti diamantu
    for i in range(size):
        print(" " * i, end = "") #lava medzera
        print("\\" * (size - i), end = "") #lava strana diamantu
        print("/" * (size - i)) #prava strana diamantu

#spustenie programu
if __name__ == "__main__":
    main()


