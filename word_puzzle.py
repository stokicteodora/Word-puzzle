# ##########################################################################################################################################################################################################################################
#  Title: Word Puzzle
# Programmer: Teodora Stokic
# Description: This program is inspired by Wordle. Users enter five-letter words to guess a randomly selected mystery word. After each guess, hints show correct letters and positions. Users have a limited number of tries.
# Date: 14.11.2025
# #########################################################################################################################################################################################################################################

import random
# Greets user and explains the rules
print("Wilkommen zu Word Puzzle!")
username = input("Wie heisst du? ")
while True:
    experienced = input("Hallo, " + username.capitalize() + "! Kennst du die Regeln? (Y/N) ")
    if experienced.lower () == "n" :
        print(
        "So funktioniert das Spiel:\n"
        "- Du musst ein fünfstelliges Wort erraten.\n"
        "- Dafür hast du insgesamt 6 Versuche.\n"
        "- Gib jedes Mal ein fünfstelliges Wort ein.\n"
        "- Die Buchstaben werden markiert:\n"
        "  - Grüner Buchstabe: richtig und an der richtigen Stelle.\n"
        "  - Gelber Buchstabe: richtig, aber an der falschen Stelle."
        )
        break
    elif experienced.lower () == "y" :
        print ("Super! Lass uns starten...")
        break
    else:
        experienced= input("Beantworte die Frage mit etweder mit y für ja oder n für nein...")

try:
    with open("wordlist.txt", "r") as file: # opens the wordlist as a file and reads it
        word_list = [line.strip() for line in file] # Creates a list of words by reading each line from the file and by removing spaces and line breaks
except:
    print("Die Datei konnte nicht gefunden werden.")

# A random word from the list gets selected
mystery_word = random.choice(word_list)

while True:
    difficulty = input("Wähle Schwierigkeitsgrad (leicht, mittel, schwer): ").lower()
    if difficulty == "leicht":
        attempts = 8
        break
    elif difficulty == "mittel":
        attempts = 6
        break
    elif difficulty == "schwer":
        attempts = 4
        break
    else:
        print ("Ungültige Eingabe.")

# Guessing game starts
while attempts > 0:
    guess = input("Gebe ein fünfstelliges Wort ein: ").upper()
    while (len(guess) != 5):
        print("Das Wort muss fünfstellig sein")
        guess = input("Gebe ein FÜNFSTELLIGES Wort ein:").upper()

    if  guess.upper() == mystery_word:
        print("Du hast das Wort erfolgreich erraten!")
        exit ()
# Feedback
    feedback = ["⚫"] * 5
    copy = list(mystery_word)

    for i in range(5):
        if guess[i] == copy[i]:
            feedback[i] = "🟢"
            copy[i] = " "

    for i in range(5):
        if feedback[i] == "⚫":
            if guess[i] in copy:
                feedback[i] = "🟡"
                copy[copy.index(guess[i])] = " " # Ai helped me with line 77

    print("".join(feedback))

    attempts -= 1
    print("Versuche übrig:", attempts)

print("Du hast verloren. Das Wort war:", mystery_word)
