from pip._vendor.distlib.compat import raw_input
import os
def main():
    print("--Wertetabellenrechner--")
    eingabe = input("y = ")

    
    x = -3
    mdrei = eval(eingabe)
    x = -2
    mzwei = eval(eingabe)
    x = -1
    meins = eval(eingabe)
    x = 0
    null = eval(eingabe)
    x = 1
    eins = eval(eingabe)
    x = 2
    zwei = eval(eingabe)
    x = 3
    drei = eval(eingabe)
    
    print("y = " + eingabe)

    print("Ergebnis: ")
    print("| -3 | -2 | -1 | 0 | 1 | 2 | 3 |")
    print("|------------------------------|")
    print("|", mdrei,"|", mzwei,"|", meins,"|", null,"|", eins,"|", zwei,"|", drei,"|")
    os.system('pause')


if __name__ == "__main__":
    main()
