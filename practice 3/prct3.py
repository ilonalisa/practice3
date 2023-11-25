import random

print("Вітаю!")
print("Правила гри: \nЯ загадую число. \nА ви намагаєтесь вгадати. ")

secret_number = random.randint(1, 50)

tries = 0  

while True:
    guess_number = int(input("Вгадайте число від 1 до 50 :) \n"))
    tries += 1  

    if guess_number == secret_number:
        break
    elif guess_number < secret_number:
        print("Замало! Спробуйте ще!")
    else:
        print("Забагато! Спробуйте ще!")

print("Вітаю з перемогою!")
print(f"Загадане число - {secret_number}.")
print(f"Ви зробили {tries} спроб.")
