from random import randint

generated_number = randint(1, 10)
while True:
    number = int(input("Podaj liczbę od 1 do 9: "))
    if number == generated_number:
        print("Odgadnąłeś liczbę, gratulacje")
        break
