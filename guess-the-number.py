
# Tebak angka gaje hohoho
# ZPP-P1 — Tebak-Angka
# Practice project again cuyy,series zpp ini mungkin berlanjut sampe beberapa tahun kedepan
# README!
# Fitur?
# - change difficulty
# - 4 difficulty

# gue saat membuat project ini, gue masih berusia 14th
# dan cita cita gue masih sama yaitu jadi AI-Engineer
# butterfly effecy: !dimulai dari langkah kecil sebelum membuat revolusi!

from random import randint
from time import sleep

print("Welcome to guess the number!")
sleep(1)

running = True
while running:
    print("\nPlease select the difficulty : ")
    print(" • Easy (1-10)\n • Normal (1-20)\n • Hard (1-50)\n • Extreme (1-100)")
    difficulty_input: str = input(">>> ").lower()
    
    keywords_d = {
        "easy": 10,
        "normal": 20,
        "hard": 50,
        "extreme": 100
    }
    
    def difficulty(max_num):
        while True:
            number = randint(1, max_num)
            answer = int(input(f"Guess The Nunber! 1-{max_num}: "))
            
            if answer == number:
                print(f"You win! The number is {number}")
            else:
                print(f"Better luck next time! The number is {number}")
            
            sleep(0.5)
            print("Wanna play again? Or wanna change the difficulty?")
            print("Yes | No | Change")
            user_input = input(">>> ").lower()
            
            if user_input == "yes":
                continue
            elif user_input == "no":
                print("Thanks for playing!")
                return "quit"
            elif user_input == "change":
                print("Back to difficulty menu...")
                sleep(1)
                return "menu"
            else:
                print("Invalid input, going back to menu...")
                return "menu"
                
    if difficulty_input in keywords_d:
        result = difficulty(keywords_d[difficulty_input])
        if result == "quit":
            running = False
    else:
        print("Invalid input!")
        sleep(1)
