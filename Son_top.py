import random

def sontop(son = 10):
    print(f"Men 1 dan {son} gacha bo'lgan son o'yladim, topa olasizmi? ")
    urinish = 0
    tasodifiy_son = random.randint(1, son)

    while True:
        taxmin = int(input(">>> "))
        urinish += 1

        if taxmin < tasodifiy_son:
            print("Xato, men kattaroq son o'yladim...")
        elif taxmin > tasodifiy_son:
            print("Xato, men kichikroq son o'yladim...")
        elif taxmin == tasodifiy_son:
            break

    print(f"To'g'ri topdingiz! {urinish} ta urinish.")
    return urinish


def sontoppc(son = 10):
    input(
        f"Siz 1 dan {son} gacha bo'lgan son o'ylab, istalgan tugmani bosing. ")
    print(
        "O'ylagan soningizdan kichik bo'lsa (-), katta bo'lsa (+) ni bosing.")
    quyi = 1
    yuqori = son
    urinish = 0

    while True:
        urinish += 1
        taxmin = random.randint(quyi, yuqori)
        javob = input(
            f"Siz o'ylagan son {taxmin}. To'g'rimi (t / +, -)? \n >>> ").lower(
            )
        if javob == "+":
            quyi = taxmin + 1
        elif javob == "-":
            yuqori = taxmin - 1
        else:
            break

    print(f"Topdim! {urinish} ta urinish.")
    return urinish



print("     Son top o'yini     ")

while True:
    son = int(input("Oraliq chegarasini kiriting: "))

    user = sontop(son)
    computer = sontoppc(son)
    
    if user < computer:
        print(f"Siz yutdingiz: {user} < {computer}.")
    elif user == computer:
        print(f"Durang: {user} = {computer}.")
    else:
        print(f"Men yutdim: {user} > {computer}.")

    yana = int(input("Yana o'ynaysizmi? Ha(1), Yo'q(0): "))
    if yana == 0:
        break

print("O'yin tugadi!")


