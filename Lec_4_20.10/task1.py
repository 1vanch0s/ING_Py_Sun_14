# Задача. В космонавты берут не всех. Берут только тех, чей рост
# НЕ МЕНЬШЕ 150 см и НЕ БОЛЬШЕ 190 см. Ваша задача - отобрать кандидатов в
# космонавты. А также узнать максимальный и минимальный рост отобранных
# кандидатов.


# На вход вашей программе подается несколько значений роста
# кандидатов в космонавты. Ввод прекращается, если было введено отрицательное
# значение роста космонавта.
# Необходимо ответить на вопросы: сколько кандидатов подходят под критерий
# становления космонавтом. А также каковы показатели МАКСИМАЛЬНОГО и МИНИМАЛЬНОГО
# роста отобранных кандидатов.

max_h = 190
min_h = 150
summ_h = 0
cand_max = -999
cand_min = 999
count = 0
h = int(input("Enter H of candidate: "))
while h >= 0:
    if h >= min_h and h <= max_h:
        count += 1
        summ += h
        if h > cand_max:
            cand_max = h
        if h < cand_min:
            cand_min = h
    h = int(input("Enter H of candidate: "))

print("Total amount of valid candidates: ", count)
print("Max H of valid candidates: ", cand_max)
print("Min H of valid candidates: ", cand_min)
print("Average H of valid candidates: ", summ_h / count)

