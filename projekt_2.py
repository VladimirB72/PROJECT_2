"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Vladimír Bořek
email: borek.vladimir@iex.cz
"""

oddelovac = "=" * 48

    # Vytvoření herního pole(desky)

deska = [[" " for _ in range(3)] for _ in range(3)]
 

    # Vytiskne uvítací zprávu

def tisk_uvitaci_zprava():
        """
        Přivítá hráče a seznámí s pravidly hry.

        """
        uvitaci_zprava = """
Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game

-------------------------------------------- 
    """
        print(uvitaci_zprava)

  



    # Funkce pro vykreslení hrací desky

def vykreslit_desku():
        """
        Vykreslí hrací pole o rozměrech 3x3, s odělovacím řádkem.

        +---+---+---+
        |   |   |   |
        +---+---+---+
        |   |   |   |
        +---+---+---+
        |   |   |   |
        +---+---+---+
        =================================================
        """
        vodorovny_radek = "+---+---+---+"

        print(vodorovny_radek)
        for radek in deska:
            print(f"| {' | '.join(radek)} |")
            print(vodorovny_radek)
        print(oddelovac)

    # Funkce pro ověření vítěze
def kontrola_viteze():
        """
        Kontrola řádků a sloupců.Test různých herních situací.
        Příklad:
        >>> ["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
        >>>  Očekávaný výstup: X

        >>> ["X", "O", "X"], [" ", "O", " "], ["X", "O", " "]]
        >>> Očekávaný výstup: O

        >>> ["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        >>> Očekávaný výstup: None
        """
        # Kontrola řádků a sloupků

        for i in range(3):
            if deska[i][0] == deska[i][1] == deska[i][2] != " ":
                return deska[i][0]
            if deska[0][i] == deska[1][i] == deska[2][i] != " ":
                return deska[0][i]

        # Kontrola diagonál

        if deska[0][0] == deska[1][1] == deska[2][2] != " ":
            return deska[0][0]
        if deska[0][2] == deska[1][1] == deska[2][0] != " ":
            return deska[0][2]

        return None

    # Hlavní herní smyčka
def main():

    tisk_uvitaci_zprava()

    hrac = "X"

    for tah in range(9):
        vykreslit_desku()

        while True:

            # Získání vstupu od hráče

            pozice_vstup = input((f"Player: {hrac} | Please enter your move number:"))

            if not pozice_vstup.isdigit():
                print("Invalid input. Enter a number BTW 1 and 9.")
                continue

            pozice = int(pozice_vstup) - 1
            if pozice < 0 or pozice >= 9:
                print("Number out of range. Enter a number BTW 1 and 9.")
                continue

            radek, sloupec = divmod(pozice, 3)
            if deska[radek][sloupec] == " ":
                deska[radek][sloupec] = hrac
                break
            else:
                print("This field is already occupied. Choose another.")

        print(oddelovac)

        # Kontrola vítěze

        vitez = kontrola_viteze()
        if vitez:
            vykreslit_desku()
            print(f"Congratulations,the player {vitez} WON!")
            print(oddelovac)
            return

        # Změna hráče

        if hrac == "X":
            hrac = "O"
        else:
            hrac = "X"

    # Pokud je deska plná a není vítěz

    vykreslit_desku()
    print("DRAW!")
    print(oddelovac)


# Spuštění programu

if __name__ == "__main__":
    main()
