# if-else condition
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
user_name = input("Ismingiz nima? >>> ").lower()
if user_name == "admin":
    print("Xush kelibsiz,", user_name.title(), ". Foydlanuvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz,", user_name.title(), "!")
print("Ikkita son kiriting: ")
son1 = int(input("1-son >>> "))
son2 = int(input("2-son >>> "))
if son1==son2:
    print("Sonlar teng.")
else:
    print("Sonlar teng emas.")
son = float(input("Istalgan son kiriting: "))
if son > 0:
    print("Son musbat.")
else:
    print("Son manfiy.")
if son >= 0:
    print("Sonning kvadrat ildizi:", son**(1/2))
else:
    print("Manfiy sondan kvadrat ildiz chiqmaydi.")

# multiple condition
juft_son = int(input(("Juft son kiriting: ")))
if juft_son%2==0:
    print("Rahmat!")
else:
    print("Bu juft emas.")
yosh = int(input("Yoshingzini kiriting: "))
if (yosh<=4 or yosh>=60) and yosh>=0:
    print("Chipta narxi: bepul")
elif yosh<18 and yosh>4:
    print("Chipta narxi: 10000 so'm")
elif yosh>=18 and yosh<60:
    print("Chipta narxi: 20000 so'm")
print("Ikkita son kiriting: ")
son1 = float(input("1-son >>> "))
son2 = float(input("2-son >>> "))
if son1>son2:
    print(f"{son1} > {son2}")
elif son1==son2:
    print(f"{son1} = {son2}")
else:
    print(f"{son1} < {son2}")
mahsulotlar = ["anor", "olma", "nok", "non", "sut", "qaymoq", "kolbasa", "pishloq", "shokolad", "suv"]
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulot: ").lower())
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot.title()} do'konimizda bor")
    else:
        print(f"{mahsulot.title()} do'konimizda yo'q.")
butun_son = int(input("Biror butun son kiriting: "))
for n in range(2, 11):
    if butun_son % n == 0:
        print(f"{butun_son} {n} ga qoldiqsiz bo'linadi.")
        



