''' Funksiya '''
def t_yilini_hisoblash():
    """ Foydalanuvchi tug'ilgan yilini hisoblaydigan funksiya """
    joriy_yil=2025
    ism = input("Ismingiz nima? ")
    yosh = int(input("Yoshingiz nechada? "))
    print(f"Salom {ism.title()}, siz {joriy_yil - yosh}-yilda tug'ilgansiz.")
t_yilini_hisoblash()

def son_darajasini_hisoblash():
    """ Kiritilgan sonning kvadrati va kubini hisoblaydigan funksiya """
    print("Salom, men sizga sonning kvadrati va kubini hisoblab beraman.")
    son = float(input("Biror son kiriting: "))
    print(f"Kvadrati: {son**2}\n"
          f"Kubi: {son**3}")
son_darajasini_hisoblash()

def juft_toqlikni_hisoblash():
    """ Butun sonning juft-toqligini hisoblaydigan funksiya """
    son = int(input("Butun son kiriting: "))
    if son%2==0:
        print("Bu son juft.")
    else:
        print("Bu son toq.")
juft_toqlikni_hisoblash()

def sonlarni_taqqoslash():
    ''' Sonlarni taqqoslash funksiyasi '''
    print("Ixtiyoriy 2 ta son kiriting >>> ")
    number1 = float(input("1-son: "))
    number2 = float(input("2-son: "))                
    if number1 > number2:
        print(f"{number1} soni katta.")
    elif number1 == number2:
        print("Sonlar teng.")
    else:
        print(f"{number2} soni katta.")
sonlarni_taqqoslash()

def sonlarni_chiqarish(x, y=2):
    print(x, end=' va ')
    print(y)
sonlarni_chiqarish(234.12)

def bolinuvchilarni_korsatish():
    son = int(input("Ixtiyoriy butun son kiriting, men sizga 2 - 10 oraliqdagi bo'linuvchilarini hisoblab beraman.\n >>> "))
    i = 0
    for n in range(2, 11):
        if son%n==0:
            print(n, end=", ")
            i+=1
    print(f"Sonning {i} ta bo'luvchisi bor.")
bolinuvchilarni_korsatish()

''' Qiymat qaytaruvchi funksiya '''
def user_info(ism, t_yil, t_joy, familya='', pochta='', telefon=''):
    ''' Foydalanuvchining ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya. '''
    user = {}
    user['ism']=ism
    user['familya']=familya
    user['t_yil']=t_yil
    user['t_joy']=t_joy
    user['pochta']=pochta
    user['telefon']=telefon
    return user
user = user_info('Muhammadjon', t_yil=2003, t_joy="Denov", telefon="91 910 43 03")

for info in user:
    print(user[info])
 
def katta_son(son1, son2, son3):
    return max(son1, son2, son3)

print(katta_son(23,123,434))

print("Aylananing parametrlarini hisoblash dasturi")
def aylanani_hisoblash():
    PI = 3.14
    radius = float(input("Aylaning radiusini kiriting: "))
    parametrlar = {
        'radius':radius,
        'diametr':radius*2,
        'perimetr':2*PI*radius,
        'yuza':PI*radius*radius
        }
    return parametrlar

print(aylanani_hisoblash())
    
def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

print(tub_sonlar_top(2, 200))

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))
       
''' Funksiya va ro'yxat '''


''' Moslashuvchan funksiya '''
def kopaytir(*sonlar):
    result = 1
    for n in sonlar:
        result*=n
    return result
print(kopaytir(1,2,3))

def talaba_info(ism, familya, **talabalar):
    talabalar['ism']=ism
    talabalar['familya']=familya
    return talabalar
print(talaba_info('Muhammadjon', 'Xudoyberdiyev', telefon='91 910 43 03', yosh=22))


















