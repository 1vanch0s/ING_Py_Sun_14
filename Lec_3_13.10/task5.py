print('h' in 'Hello world!')

# ЗАДАЧА
# РЕГИСТАЦИЯ КЛИЕНТА: Пользователь вводит свои данные :
# адрес электронной почты и пароль. Если в адресе эл.почты отсутствует символ
# '@' --- программа сообщает об ошибке 'ERROR: INVALID Email'
# В противном случае - программа печатает 'REGISTRATION COMPLETED'

# Пример работы:
# Ввод                                        # Вывод
# kek@lol.ru
# 12356                                       REGISTRATION COMPLETED

# qwerelkj.com
# 765433245567                                ERROR: INVALID Email 


while True:
    email = input()
    password = input()

    if '@' in email:
        print("REGISTRATION COMPLETED")
        break
    else:
        print("ERROR: INVALID Email| TRY AGAIN")

print("ALLES")

