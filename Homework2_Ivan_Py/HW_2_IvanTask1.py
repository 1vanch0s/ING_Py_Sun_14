letter = input("Введите сообщение: ")
value = len(letter) * 23
rub = value // 100
kop = value % 100
print(rub , "руб." , kop , "коп.")

