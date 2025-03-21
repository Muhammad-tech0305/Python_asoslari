# Python keywords:
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not                 

# O'zgaruvchilar darsi
salom = "Hello World!"
print(salom)
xabar = "Men dotNet kasbini o'rganyapman."
print(xabar)
xabar = "Lekin, hozir Python tilini o'rganyapman."
print(xabar)
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi", radius, "ga teng,", "yuzi esa", aylana_yuzi, "ga teng.")

# Sonlar darsi
# Amaliyot
# 1
son = int(input("Istalgan son kiriting: "))
kv = son**2
kub = son**3
print(f"{son} ning kvadrati {kv} ga teng \n{son} ning kubi {kub} ga teng")
# 2
yosh = int(input("Yoshingiz nechada >>> "))
print(f"Siz {2025 - yosh}-yilda tug'ilgansiz.")

# Listlar bilan ishlash darsi
# Amaliyot
davlatlar = ["Amerika", "Rossiya", "Yaponiya", "Angliya", "Turkiya"]
print("Ro'yxatning uzunligi:", len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse = True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse = True)
print(davlatlar)
juft_sonlar = list(range(120, 1201, 2))
print(sum(juft_sonlar))
print(max(juft_sonlar) - min(juft_sonlar))
print("Ro'yxat uzunligi:", len(juft_sonlar))
print(juft_sonlar[:20])
print(juft_sonlar[530:550])
print(juft_sonlar[-20:])
taomlar = ["Qaymoq va non", "Sho'rva", "Osh", "Pishloq va sut", "Somsa"]
nonushta = taomlar[:]
nonushta.remove("Sho'rva")
nonushta.remove("Osh")
nonushta.remove("Somsa")
nonushta.append("Smetana va quymoq")
nonushta.append("Tuxum")
print(taomlar)
print(nonushta)

# for loop darsi
ismlar = ["Fayoz", "Fazliddin", "Ubaydullo", "Muslim", "Fotih"]
for ism in ismlar:
    print("Salom,", ism)
print("Kod", len(ismlar), "marta takrorlandi.")
toq_sonlar = list(range(11, 100, 2))
for toq_son in toq_sonlar:
    print("Kub daraja:", toq_son**3)
kinolar = []
print("Sevimli filmlaringiz kiriting (5 ta): ")
for n in range(5):
    kinolar.append(input(f"{n+1}-film: "))
print("Sevimli filmlaringiz >>>", kinolar)
uchrashuv = int(input("Bugun nechta odam bilan suhbatlashdingiz? >>> "))
uchrashganlar = []
print("Uchrashgan odamlaringiz ismlarini yozing: ")
for n in range(1, uchrashuv):
    uchrashganlar.append(input(f"{n}-odam: "))
print ("Uchrashuvlar ro'yxati >>>", uchrashganlar)
