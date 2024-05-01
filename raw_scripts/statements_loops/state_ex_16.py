dog_age = int(input("Podaj wiek psa: "))

if dog_age < 0:
    print("Wiek musi być liczbą większą od 0")
    exit()
elif dog_age <= 2:
    dog_age_in_human = dog_age * 10.5
else:
    dog_age_in_human = 21 + (dog_age - 2) * 4

print(f"Wiek psa w latach ludzkich wynosi: {dog_age_in_human}")
