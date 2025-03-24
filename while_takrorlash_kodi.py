# input() va while
# kitoblar = []
# n = 1
# while True:
#     kitob = input(f'Sevimli kitobingizni kiriting (tugatish uchun \'stop\' deb yozing): \n {n}. ').lower()
#     if kitob == 'stop':
#         break
#     kitoblar.append(kitob)
#     n += 1
# print(kitoblar)
# print("Dastur tugadi.")

# ishora = True
# while ishora:
#     yosh = input("Muzeyga xush kelibsiz, yoshingizni kiriting (tugatish uchun 'exit' yoki 'quit' kiriting): ")
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     if int(yosh) < 7 and int(yosh) >= 0:
#         print("Sizga chipta narxi 2000 so'm.")
#     elif int(yosh) < 18 and int(yosh) >= 7:
#         print("Sizga chipta narxi 3000 so'm.")
#     elif int(yosh) >= 18 and int(yosh) < 65:
#         print("Sizga chipta narxi 10000 so'm.")
#     elif int(yosh) >= 65 and int(yosh) < 150:
#         print("Sizga kirish bepul.")
#     else:
#         print("Bunday yosh yo'q.")
# print("Dastur tugadi.")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
# while sikli, ro'yxatlar va lug'atlar
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     n += 1
#     takrorlash = input("Yana ism qo'shasizmi (ha/yo'q)? ")
#     if takrorlash != 'ha':
#         break

# for ism in ismlar:
#     print(ism.title(), end=", ")
    
print("\n \t Bu sizning e-bozor dasturingiz \t")
bozor = {}
tugatish = True
while tugatish:
    mahsulot = input("Mahsulotingizni kiriting: ").lower()
    narx = int(input("Narxini kiriting (so'm): "))
    bozor[mahsulot] = narx
    savol = input(("Tugatasizmi (ha/yo'q)? >>> ")).lower()
    if savol == 'ha':
        tugatish = False
        break
print(bozor)

print("\n \t Bu taom buyurtma qilish dasturi \t")
buyurtmalar = []
n = 1
savol = "Nima ovqat buyurtma qilasiz? >>> "
print(savol)
while True:
    buyurtma = input(f"{n}-buyurtma: ").lower()
    buyurtmalar.append(buyurtma)
    n+=1
    tugatish = input("Tugatasizmi (ha/yo'q)? ").lower()
    if tugatish == 'ha':
        break
print("Sizning buyurtmalaringiz: ")
for buyurtma in buyurtmalar:
    print(buyurtma.capitalize(), end=": ")
    if buyurtma in bozor:
        print(bozor[buyurtma], " so'm ")
    elif buyurtma not in bozor:
        print("bizda bu mahsulot yo'q.")

        