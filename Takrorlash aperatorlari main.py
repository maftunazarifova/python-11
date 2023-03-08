# for son in range(1,100):
#     print(son)


# for SON in range(16):
#     print(SON)
# else:
#     print("Finally finished!")

# for i in range(1, 11, 1):
#     for j in range(1, 11, 1):
#         print(f"{i} * {j} = {i * j}")
#     print("\n")

# a = "banana"
# b = iter(a)
# print(next(b)) # b
# print(next(b)) # a
# print(next(b)) # n
# print(next(b)) # a
# print(next(b)) # n
# print(next(b)) # a

# Shartga qarab tsiklni ishlatish!
# a = 1
# while a < 8:
#     print(a)
#     a += 1

# # Cheksiz tsikl!
# while True:
#     print("Working!")

# Tsiklni shartga qarab to'xtatish!
# a = 1
# while a < 6:
#     print(a)
#     if a == 3:
#         break
#     a += 1

# Shart bo'yicha tashlab ketish!

# Shart bo'yicha tashlab ketish!
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

#kompyuter o'ylagan sonni toping:
# import random
# r_comp = int(input("Qanchagacha son o'ylasin?: "))
# comp = random.randint(1, r_comp + 1)
# urinishlar_soni = 0
# print(f"ПРИВЕТ!, men 1 dan {r_comp} gacha raqamni o'ylayapman")
# while True:
#     urinishlar_soni += 1
#     user = int(input("Taxmin qilib ko'ring!"))
#     if user == comp:
#         print(f"{urinishlar_soni} - urinish. Siz to'g'ri topdingiz. {urinishlar_soni} marta urinib!")
#         break
#     elif user > comp:
#         print(f"{urinishlar_soni} - urinish. Siz o'ylagan son men o'ylagan sondan katta!")
#     elif user < comp:
#         print(f"{urinishlar_soni} - urinish. Siz o'ylagan son men o'ylagan sondan kichik!")