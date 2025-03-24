# Lug'at (Dictionary)
onam = {'ismi':'zulfiya xudoyberdiyeva', 'tavallud yili':1970, 'shahri':'denov'}
print(f"Mening onam {onam['ismi'].title()}\
 {onam['tavallud yili']}-yilda\
 {onam['shahri'].capitalize()} tumanida tug'ilgan.")

taomlar = {
    'fayoz':'tuxum',
    'jo\'rabek aka':'kolbasa',
    'safar aka':'manti',
    'onam':'shashlik',
    'dadam':'chalob',
    'men':'osh'
    }
for ism in taomlar:
    print(f"{ism.capitalize()} {taomlar[ism]}ni yaxshi ko'radi.")
    
python_dictionary = {
    'int':'butun son (integer)',
    'float':'kasr son',
    'string':'matn',
    'input':'kiritish operatori',
    'if-else':'shart operatori (agar-yo\'qsa)',
    'for':'takrorlash operatori',
    'dictionary':'lug\'at',
    'list':'ro\'yxat',
    'variable':'o\'zgaruvchi',
    'value':'qiymat',
    'print':'chop etish',
    'tuple':'o\'zgarmas ro\'yxat'
    } 
print(f"Mening lug'atim:\n{python_dictionary}") 
      
termin = input("Terminni kiriting: ").lower()
print(python_dictionary.get(termin, "Bunday atama mavjud emas.").capitalize())
if termin in python_dictionary:
    print(python_dictionary[termin].capitalize())
else:
    print("Bunday atama mavjud emas.")

# Lug'at elementlari bilan ishlash
for key, value in python_dictionary.items():
    print(f"{key.capitalize()}: {value.capitalize()}.")
    
davlatlar = {
    'o\'zbekiston': 'toshkent',
    'angliya':'london',
    'amerika':'vashington',
    'yaponiya':'tokiyo',
    'fransiya':'parij',
    'turkiya':'anqara',
    'eron':'tehron'
    }
print(sorted(davlatlar.keys()))
print(sorted(davlatlar.values()))
      
davlat = input("Istalgan davlatni kiriting: ")
print(davlatlar.get(davlat, "Bizning ro'yxatda bunday davlat yo'q.").capitalize())      
      
buyurtma = input("Taomni kiriting: ")
menyu = {
    'osh':30_000,
    'manti':20_000,
    'somsa':12_000,
    'bishteks':33_000,
    'sho\'rva':16_000
    }     
if buyurtma in menyu: 
    print(f"{buyurtma.capitalize()} narxi {menyu[buyurtma]} so'm.")
else:
    print(f"{buyurtma.capitalize()} - bunday ovqat bizda yo'q.")

print(sum(menyu.values())) 

# Nesting
davlatlar = {
    'o\'zbekiston':{
        'poytaxt':'toshkent',
        'maydon':448_978,
        'aholi':37_543_000,
        'valyuta':'uzs'
        },
    'amerika':{
        'potaxt':'vashington',
        'maydon':9_833_520,
        'aholi':347_275_000,
        'valyuta':'usd'
        },
    'britaniya':{
        'poytaxt':'london',
        'maydon':244_820,
        'aholi':69_551_000,
        'valyuta':'gbp'
        },
    'yaponiya':{
        'poytaxt':'tokiyo',
        'maydon':377_976,
        'aholi':126_000_000,
        'valyuta':'jpy'
        }
    }
for davlat, info in davlatlar.items():
    print(f" < {davlat.capitalize()} haqida > ")
    print(f"Maydoni: {info['maydon']} kv.km ")
    print(f"Aholi soni: {info['aholi']} kishi")
    print(f"Valyutasi: {info['valyuta'].upper()}")      

davlat = input("Istalgan davlatni kiriting: ").lower()
if davlat in davlatlar:
    print(davlatlar[davlat])
else:
    print("Bunday davlat yo'q.")
    
