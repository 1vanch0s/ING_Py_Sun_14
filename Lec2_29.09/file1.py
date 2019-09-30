#print("Hello World!")

#cd -- change dir 
#dir --- directory -- что в директории (в папке)



# 1.ПЕРЕМЕННЫЕ
# Переменная - элементарная область памяти, способная хранить информацию.
# Адрес, хранимое значение 
# Название переменной == адрес
# Хранимое значение????


# 2. БАЗОВЫЕ ТИПЫ ДАННЫХ
# 2.1 ЦЕЛЫЕ ЧИСЛА (INTEGER , INT)
my_int = 10  # адрес ПРИСВОИТЬ значение
another_int = -50
ANOTHER_INT = -60
temp = 20
temp = 40 #ПЕРЕПРИСВАИВАНИЕ

# 2.2 НЕЙМИНГ
lol = 123243
_lol = 1232435465
Lol = 123

# 2.3 АРИФМЕТИКА

my_c = 10
my_d = 20
my_e = my_c + my_d
#print(my_e)


# +, *, -, /

print(25 + 36 + 42)
print(50 - 85)
print(5 * 7)
print(10 / 3)

print((10 + 20)*2/4)

print( 2**10 )


# 2.4 ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ (ДРОБНЫЕ ЧИСЛА, FLOAT)
my_float = 10.25
my_float2 = 25.23

print(my_float + my_float2)
print(2 + 10.25)

print( 15 == 15.0)

# 2.5 Логический тип данных (Булев тип, Bool)

t_bool = True  # 1 
f_bool = False # 0 

print(t_bool + f_bool*t_bool)

# Логическое сложение , Логическое умножение --- > Логический тип
# Таблица Истиности
# Логическое сложение (OR или)
print( True or True)  # 1 + 1 = 1 -- > True
print( True or False) # 1 + 0 = 1 -- > True 
print( False or True) # 0 + 1 = 1 --> True
print( False or False) # 0 + 0 = 0 -- > False


#Логическое умножение (AND и)
print( True and True)  # 1 * 1 = 1 -- > True
print( True and False) # 1 * 0 = 0 -- > False
print( False and True) # 0 * 1 = 0 --> False
print( False and False) # 0 * 0 = 0 --> False





# 2.6 СТРОКИ 
# Строка - последовательность символов
my_string = "Hello WORL!24 '354234' 3542@#@@#!!4K"
my_string2 = 'Qwerty12435'

# Конкатенация строк (сложение строк)
print(my_string + my_string2)

f = 'a'
q = ''



# 2.7 НИЧЕГО
t_none = None 


#False == 0 == None
#True -- все остальное  

print("#####################################")
print("_________________Base type_____________")
a = 1000
print( type(a) , a.__sizeof__(), a)
b = 10.01
print(type(b), b.__sizeof__(), b)
c = True 
print(type(c), c.__sizeof__(), c)
d = "Qwertylkhjghfgdffgfhghjkljkhjghfgfdsdfghjkljhjghfdsdfgguioiuytrew"
print(type(d), d.__sizeof__(), d)
e = None 
print(type(e), e.__sizeof__(), e)
print("###########################################")
@Vlasov_Evgeny
