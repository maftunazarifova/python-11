## DARS REJASI ##

# 1. ----
# 2. ----
# 3. ----
# 4. ----
# 5. ----
# 6. ----
# 7. ----

###############################################################################################
#amaliy topshiriq
#1.Foydalanuvchidan ismini so'rash
#2.Kim o'ylashini tanlash
#3.Agar kompyuter o'ylasa, nechagacha o'ylashini kiritish
#4.Agar foydalanuvchi o'ylasa, nechagacha o'ylashini kiritish
#5.Shart tekshirish: o'ylangan sondan katta yoki kichik bo'lgan holda
#6.Agar shart to'g'ri bo'lsa "Topdingiz", aks holda "Qayta urinib ko'ring xabari terminalga chiqsin"
#7.Necha marta urinib topganligini ko'rsatish
#8.Dastur tugagach qayta ishga tushsin

# import  random
# Ismi = input("Salom, sizning ismingiz nima. \n>>> ")

# while True:

#     print(f"Salom {Ismi}. \nKodni siz kiritgan son va harflar bo'yicha yaratayhmi yoki o'zim ixtiyoriy yarataymi? \nAgar O'zim tanlasam [1] ni bosing \n Agar Foydalanuvchi tanlasa [2] ni bosing")
#     tanlov = int(input(">>> "))
#     if tanlov == 1:
#         lower_case = "abcdefghijklmnopqrstuvwxyz"
#         upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'"
#         symbol = "!@#$%^&*(){}[]_+="
#         num = "0123456789"

#         ans = lower_case + upper_case + symbol + num

#         length = input("Necha xonali son kerak: ")
#         password = "".join(random.sample(ans,length))
#         print("Sizning kodingiz. \n>>> ", password)

#     elif tanlov == 2:
#         lower_case = input("Harflarni kiriting: \n>>>")
#         symbol = input(f"symbolni tanlang: \n>>> ")
#         num = int(input("raqamlarni kiriting: \n>>> "))

#         ans = lower_case + symbol + num

#         length = input("Necha xonali son kerak: ")
#         password = "".join(random.sample(ans,length))
#         print("Sizning kodingiz. \n>>> ", password)
#     else:
#         print("bu son qabul qilinmadi: ")


############################################################################################################

#6-dars
#1. Funksiya - bir qancha amallar va bayonotlarni bitta alohida qismga ajratib olish! Bankomat.

#2. Salom beruvchi funksiya.

# def salom_ber():
#     print("Assalomu alaykum")

# #Funksiya chaqirish
# salom_ber()

# #ob-havoni aniqlab ber.
# def obhavo(gradus): #gradus-funksiya uchun argument.
#     if gradus <= 10:
#         return "Obhavo salqin!"
#     elif 10 < gradus<= 25:
#         return("Obhavo iliq!")
#     else:
#         return "Obhavo issiq!"
# print(obhavo(5))

##################################################################################
#unli va undoshni aniqlash (+simvollar va solarni ham aniqlaydi)
# def belgilar(matn):

#     unlilar = "aeiou"
#     undoshlar = "bdfghjklmnpqrstvxyz"
#     simvollar = """!@#$%^&*()_№;%:?*/\[]{}-"""
#     raqamlar = "0123456789"
    
#     matn = matn.lower()

#     unli_soni = 0
#     undosh_soni = 0
#     simvol_soni = 0
#     raqmlar_soni = 0

#     # Tsikl yordamida har bitta harf bo'ylab matnni yurib chiqish.
#     for harf in matn.lower():
#         if harf in unlilar:
#             unli_soni += 1
#         elif harf in undoshlar:
#             undosh_soni += 1
#         elif harf in simvollar:
#             simvol_soni += 1
#         elif harf in raqamlar:
#             raqamlar_soni += 1

# # Natijani bizga qaytarib bersin
#     return f"Ushbu textda {unli_soni} dona unli son, {undosh_soni} dona undosh son, {simvol_soni} dona simvol son va {raqamlar_soni} dona raqmlar soni mavjud."

# # Funksiyani ishlatamiz.
# print(belgilar("Uzbekistan"))

# FIZZBUZZ ni funksiya yordamida ishlatish.


# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return"FIZZBUZZ"
#     elif num % 3 == 0:
#         return "FIZZ"
#     elif num % 5 == 0:
#         return "BUZZ"
#     else:
#         return num

# print(fizzbuzz(3))
# print(fizzbuzz(5))
# print(fizzbuzz(15))
# print(fizzbuzz(17))

#########################################################################################

# #Bir qatorda funksiyani e'lon qilish.
# calc = lambda a, b, c,: eval(f"{a}{b}{c}")
# print(calc(12, 13, "+"))
# 
